import os
import tkinter as tk
from tkinter import messagebox
from typing import List, Optional, Tuple
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from PIL import Image, ImageTk
import google.generativeai as genai

# Constants (same as in the original code)
STROKE_GESTURE: List[int] = [0, 1, 0, 0, 0]
CLEAR_GESTURE: List[int] = [1, 0, 0, 0, 0]
SUBMIT_GESTURE: List[int] = [1, 1, 1, 1, 0]
PROMPT_TEXT = "Solve this math problem"
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
CAMERA_INDEX = 1
LINE_COLOR = (255, 0, 255)
LINE_THICKNESS = 10
MODEL_NAME = "gemini-1.5-flash"


def configure_model() -> Optional[genai.GenerativeModel]:
    """Initialize the Gemini model."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        messagebox.showerror("Error", "Google API key not found.")
        return None
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def create_capture(index: int = CAMERA_INDEX) -> Optional[cv2.VideoCapture]:
    """Create video capture."""
    capture = cv2.VideoCapture(index)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    if not capture.isOpened():
        messagebox.showerror("Error", f"Unable to access camera at index {index}.")
        return None
    return capture

def create_detector() -> HandDetector:
    """Return a hand detector tuned for single-hand interactions."""
    return HandDetector(
        staticMode=False,
        maxHands=1,
        modelComplexity=1,
        detectionCon=0.7,
        minTrackCon=0.5,
    )

def detect_hand(detector: HandDetector, frame: np.ndarray) -> Optional[Tuple[List[int], List]]:
    """Detect hand and return finger states and landmarks."""
    hands, _ = detector.findHands(frame, draw=False, flipType=True)
    if not hands:
        return None
    hand = hands[0]
    fingers = detector.fingersUp(hand)
    return fingers, hand["lmList"]

def draw_on_canvas(
    fingers: List[int],
    landmarks: List,
    canvas: np.ndarray,
    previous_point: Optional[Tuple[int, int]],
) -> Optional[Tuple[int, int]]:
    """Draw on the canvas using OpenCV."""
    if fingers == STROKE_GESTURE:
        pen_point = tuple(landmarks[8][0:2])
        if previous_point is None:
            previous_point = pen_point
        cv2.line(canvas, pen_point, previous_point, LINE_COLOR, LINE_THICKNESS)
        return pen_point

    if fingers == CLEAR_GESTURE:
        canvas[:] = 0
        return None

    return None

def query_model(model: genai.GenerativeModel, canvas: np.ndarray, fingers: List[int]) -> Optional[str]:
    """Send canvas to Gemini and get a response."""
    if fingers != SUBMIT_GESTURE:
        return None

    rgb_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_canvas)

    response = model.generate_content([PROMPT_TEXT, pil_image])
    return getattr(response, "text", None)

def update_frame(frame: np.ndarray, canvas: np.ndarray) -> ImageTk.PhotoImage:
    """Update the frame with the canvas."""
    composed = cv2.addWeighted(frame, 0.7, canvas, 0.3, 0.0)
    return ImageTk.PhotoImage(image=Image.fromarray(composed))

def main() -> None:
    """Main Tkinter application loop."""
    root = tk.Tk()
    root.title("Math Gesture Solver")

    frame_window = tk.Label(root)
    frame_window.pack()

    output_label = tk.Label(root, text="Answer: ", font=("Arial", 12))
    output_label.pack()

    model = configure_model()
    detector = create_detector()
    capture = create_capture()

    if not (model and capture):
        root.quit()
        return

    canvas: Optional[np.ndarray] = None
    last_point: Optional[Tuple[int, int]] = None
    latest_text: Optional[str] = None

    def update_video():
        """Capture video frames and process gestures."""
        nonlocal last_point, latest_text, canvas

        success, frame = capture.read()
        if not success:
            messagebox.showerror("Error", "Failed to read from camera.")
            root.quit()
            return

        frame = cv2.flip(frame, 1)
        if canvas is None:
            canvas = np.zeros_like(frame)

        detection = detect_hand(detector, frame)
        if detection:
            fingers, landmarks = detection
            last_point = draw_on_canvas(fingers, landmarks, canvas, last_point)
            response_text = query_model(model, canvas, fingers)
            if response_text:
                latest_text = response_text
        else:
            last_point = None

        # Update Tkinter display with new frame
        frame_image = update_frame(frame, canvas)
        frame_window.config(image=frame_image)
        frame_window.image = frame_image  # Keep a reference

        if latest_text:
            output_label.config(text=f"Answer: {latest_text}")

        root.after(10, update_video)  # Call update_video every 10ms

    update_video()  # Start the video loop
    root.mainloop()

if __name__ == "__main__":
    main()
