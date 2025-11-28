import random
import time
import tkinter as tk
from tkinter import messagebox
from typing import List, Optional, Tuple

import cv2
import mediapipe as mp
from PIL import Image, ImageTk

# Camera configuration
CAMERA_INDEX = 0
FRAME_WIDTH = 200
FRAME_HEIGHT = 200

# Outcome rules
WIN_RULES = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

# Timing configuration
STABLE_FRAME_COUNT = 8  # Number of consecutive frames required to confirm a gesture
COOLDOWN_SECONDS = 2.0


def create_capture(index: int = CAMERA_INDEX) -> Optional[cv2.VideoCapture]:
    capture = cv2.VideoCapture(index)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    if not capture.isOpened():
        messagebox.showerror("Camera Error", f"Unable to access camera at index {index}.")
        return None
    return capture


def create_detector() -> mp.solutions.hands.Hands:
    return mp.solutions.hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.5,
        model_complexity=1,
    )


def _fingers_up(landmarks: List[Tuple[int, int]]) -> List[int]:
    tips = [4, 8, 12, 16, 20]
    fingers = [0, 0, 0, 0, 0]

    # Thumb: compare x coordinate because image already flipped.
    if landmarks[tips[0]][0] > landmarks[tips[0] - 1][0]:
        fingers[0] = 1

    # Other fingers: tip y should be above pip joint.
    for idx, tip in enumerate(tips[1:], start=1):
        if landmarks[tip][1] < landmarks[tip - 2][1]:
            fingers[idx] = 1
    return fingers


def detect_hand(detector: mp.solutions.hands.Hands, frame) -> Optional[Tuple[List[int], List[Tuple[int, int]]]]:
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detector.process(rgb)
    if not results.multi_hand_landmarks:
        return None

    hand_landmarks = results.multi_hand_landmarks[0]
    h, w, _ = frame.shape
    landmark_points: List[Tuple[int, int]] = []
    for lm in hand_landmarks.landmark:
        landmark_points.append((int(lm.x * w), int(lm.y * h)))

    fingers = _fingers_up(landmark_points)
    return fingers, landmark_points


def classify_move(fingers: List[int]) -> Optional[str]:
    extended = sum(fingers)
    if extended <= 1:
        return "rock"
    if extended >= 4:
        return "paper"
    if fingers[1] and fingers[2] and not fingers[3] and not fingers[4]:
        return "scissors"
    return None


def decide_winner(player_move: str, system_move: str) -> str:
    if player_move == system_move:
        return "draw"
    if WIN_RULES[player_move] == system_move:
        return "player"
    return "system"


def main() -> None:
    root = tk.Tk()
    root.title("Rock-Paper-Scissors Hands Free")

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    main_frame.columnconfigure(0, weight=3)
    main_frame.columnconfigure(1, weight=2)
    main_frame.rowconfigure(0, weight=1)

    video_frame = tk.Frame(main_frame, bg="black", bd=0, relief="sunken")
    video_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)

    video_label = tk.Label(video_frame, bg="black")
    video_label.pack(fill="both", expand=True)

    info_frame = tk.Frame(main_frame, padx=20, pady=20)
    info_frame.grid(row=0, column=1, sticky="nsew", pady=10, padx=(0, 10))
    info_frame.columnconfigure(0, weight=1)

    status_label = tk.Label(
        info_frame,
        text="Tekan 'Mulai' lalu tunjukkan gesture Anda.",
        font=("Arial", 12),
        justify="left",
        wraplength=260,
    )
    status_label.grid(row=0, column=0, sticky="w")

    score_label = tk.Label(info_frame, text="Player 0 : 0 System", font=("Arial", 12, "bold"))
    score_label.grid(row=1, column=0, sticky="w", pady=(12, 0))

    pending_label = tk.Label(info_frame, text="Gesture terbaca: -", font=("Arial", 12))
    pending_label.grid(row=2, column=0, sticky="w", pady=(12, 0))

    player_move_label = tk.Label(info_frame, text="Gesture Anda: -", font=("Arial", 14, "bold"))
    player_move_label.grid(row=3, column=0, sticky="w", pady=(20, 0))

    computer_move_label = tk.Label(info_frame, text="Pilihan Komputer: -", font=("Arial", 14, "bold"))
    computer_move_label.grid(row=4, column=0, sticky="w", pady=(12, 0))

    result_label = tk.Label(info_frame, text="Hasil: -", font=("Arial", 16, "bold"), fg="#1d7a46")
    result_label.grid(row=5, column=0, sticky="w", pady=(20, 0))

    capture = create_capture()
    if capture is None:
        root.destroy()
        return

    detector = create_detector()

    state = {
        "round_active": False,
        "pending_move": None,
        "pending_count": 0,
        "last_result": "",
        "player_score": 0,
        "system_score": 0,
        "cooldown_until": 0.0,
        "latest_fingers": [0, 0, 0, 0, 0],
        "player_move": None,
        "system_move": None,
    }

    def format_move(move: Optional[str]) -> str:
        return move.upper() if move else "-"

    def update_score_label() -> None:
        score_label.config(text=f"Player {state['player_score']} : {state['system_score']} System")

    def start_round() -> None:
        now = time.time()
        if now < state["cooldown_until"]:
            wait_time = max(0, state["cooldown_until"] - now)
            status_label.config(text=f"Tunggu {wait_time:.1f}s sebelum ronde berikutnya.")
            return
        state["round_active"] = True
        state["pending_move"] = None
        state["pending_count"] = 0
        state["last_result"] = ""
        state["latest_fingers"] = [0, 0, 0, 0, 0]
        state["player_move"] = None
        state["system_move"] = None
        status_label.config(text="Tunjukkan ROCK / PAPER / SCISSORS di depan kamera.")
        pending_label.config(text="Gesture terbaca: -")
        player_move_label.config(text="Gesture Anda: -")
        computer_move_label.config(text="Pilihan Komputer: -")
        result_label.config(text="Hasil: -")

    def reset_scores() -> None:
        state["player_score"] = 0
        state["system_score"] = 0
        state["last_result"] = ""
        state["round_active"] = False
        state["pending_move"] = None
        state["pending_count"] = 0
        state["latest_fingers"] = [0, 0, 0, 0, 0]
        state["player_move"] = None
        state["system_move"] = None
        update_score_label()
        status_label.config(text="Skor direset. Tekan 'Mulai' untuk bermain.")
        pending_label.config(text="Gesture terbaca: -")
        player_move_label.config(text="Gesture Anda: -")
        computer_move_label.config(text="Pilihan Komputer: -")
        result_label.config(text="Hasil: -")

    def resolve_round(player_move: str) -> None:
        system_move = random.choice(["rock", "paper", "scissors"])
        winner = decide_winner(player_move, system_move)

        if winner == "player":
            state["player_score"] += 1
            result_text = f"Anda menang! {player_move.upper()} mengalahkan {system_move.upper()}."
            result_heading = "Anda MENANG!"
            result_color = "#1d7a46"
        elif winner == "system":
            state["system_score"] += 1
            result_text = f"Sistem menang! {system_move.upper()} mengalahkan {player_move.upper()}."
            result_heading = "Komputer MENANG!"
            result_color = "#b22222"
        else:
            result_text = f"Seri! Anda dan sistem memilih {player_move.upper()}."
            result_heading = "Seri!"
            result_color = "#aa7a00"

        state["player_move"] = player_move
        state["system_move"] = system_move
        state["last_result"] = result_text
        update_score_label()
        pending_label.config(text="Gesture terbaca: -")
        player_move_label.config(text=f"Gesture Anda: {format_move(state['player_move'])}")
        computer_move_label.config(text=f"Pilihan Komputer: {format_move(state['system_move'])}")
        result_label.config(text=result_heading, fg=result_color)
        status_label.config(text=result_text + " Tekan 'Mulai' untuk ronde berikutnya.")
        state["round_active"] = False
        state["pending_move"] = None
        state["pending_count"] = 0
        state["cooldown_until"] = time.time() + COOLDOWN_SECONDS

    def on_close() -> None:
        capture.release()
        detector.close()
        root.destroy()

    def update_frame() -> None:
        success, frame = capture.read()
        if not success:
            status_label.config(text="Gagal membaca kamera. Periksa perangkat Anda.")
            root.after(500, update_frame)
            return

        frame = cv2.flip(frame, 1)

        move_detected = None
        if state["round_active"]:
            detection = detect_hand(detector, frame)
            if detection:
                fingers, _ = detection
                state["latest_fingers"] = fingers
                move_detected = classify_move(fingers)
                pending_label.config(text=f"Gesture terbaca: {format_move(move_detected)}")
                if move_detected:
                    if move_detected == state["pending_move"]:
                        state["pending_count"] += 1
                    else:
                        state["pending_move"] = move_detected
                        state["pending_count"] = 1

                    if state["pending_count"] >= STABLE_FRAME_COUNT:
                        resolve_round(move_detected)
            else:
                state["pending_move"] = None
                state["pending_count"] = 0
                state["latest_fingers"] = [0, 0, 0, 0, 0]
                pending_label.config(text="Gesture terbaca: -")
        else:
            state["pending_move"] = None
            state["pending_count"] = 0
            state["latest_fingers"] = [0, 0, 0, 0, 0]
            pending_label.config(text="Gesture terbaca: -")

        # Overlay status information on the frame
        info_text = state["last_result"] if state["last_result"] else "Tekan 'Mulai' untuk memulai."
        cv2.putText(frame, info_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (20, 220, 20), 2)
        if state["round_active"]:
            prompt_text = f"Gesture terbaca: {state['pending_move'] or '...'} | jari: {state['latest_fingers']}"
        else:
            prompt_text = "Ronde belum dimulai."
        cv2.putText(frame, prompt_text, (20, FRAME_HEIGHT - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = ImageTk.PhotoImage(Image.fromarray(image))
        video_label.configure(image=image)
        video_label.image = image

        root.after(15, update_frame)

    button_frame = tk.Frame(info_frame)
    button_frame.grid(row=6, column=0, sticky="w", pady=(30, 0))

    start_button = tk.Button(button_frame, text="Mulai", command=start_round, width=12)
    start_button.grid(row=0, column=0, padx=(0, 10))

    reset_button = tk.Button(button_frame, text="Reset Skor", command=reset_scores, width=12)
    reset_button.grid(row=0, column=1)

    root.protocol("WM_DELETE_WINDOW", on_close)
    update_frame()
    root.mainloop()


if __name__ == "__main__":
    main()
