from __future__ import annotations

import os
from pathlib import Path
from typing import List, Optional, Tuple

import cv2
import numpy as np
import streamlit as st
from cvzone.HandTrackingModule import HandDetector
from PIL import Image
import google.generativeai as genai
from streamlit.errors import StreamlitSecretNotFoundError

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
BASE_DIR = Path(__file__).resolve().parent
BANNER_CANDIDATES = [
    BASE_DIR / "MathGestures.png",
    BASE_DIR / "assets" / "MathGestures.png",
    BASE_DIR / "banner.png",
    BASE_DIR / "assets" / "banner.png",
]


def configure_model() -> Optional[genai.GenerativeModel]:
    """Initialise the Gemini model using the API key from secrets or environment."""
    api_key = os.getenv("GOOGLE_API_KEY")
    try:
        secret_key = st.secrets["GOOGLE_API_KEY"]
    except (KeyError, StreamlitSecretNotFoundError):
        secret_key = None

    if secret_key:
        api_key = secret_key

    if not api_key:
        st.error("Google API key not found. Set `GOOGLE_API_KEY` in secrets or the environment.")
        return None

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)


def create_capture(index: int = CAMERA_INDEX) -> Optional[cv2.VideoCapture]:
    """Create, configure, and validate the video capture device."""
    capture = cv2.VideoCapture(index)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    if not capture.isOpened():
        st.error(f"Unable to access camera at index {index}.")
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
    """Detect a hand and return the finger states plus landmarks."""
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
    """Handle drawing and clearing gestures and return the updated pen location."""
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
    """Send the current canvas to Gemini when the submit gesture is detected."""
    if fingers != SUBMIT_GESTURE:
        return None

    rgb_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_canvas)

    response = model.generate_content([PROMPT_TEXT, pil_image])
    return getattr(response, "text", None)


def main() -> None:
    st.set_page_config(layout="wide")
    for banner_path in BANNER_CANDIDATES:
        if banner_path.exists():
            st.image(str(banner_path))
            break
    else:
        st.warning("Banner image not found. Add one at `assets/banner.png` to customise the header.")

    col1, col2 = st.columns([3, 2])
    with col1:
        run = st.checkbox("Run", value=True)
        frame_window = st.image([])

    with col2:
        st.title("Answer")
        output_text_area = st.empty()

    model = configure_model()
    detector = create_detector()
    capture = create_capture()

    if not (model and capture):
        st.stop()

    canvas: Optional[np.ndarray] = None
    last_point: Optional[Tuple[int, int]] = None
    latest_text: Optional[str] = None

    while True:
        if not run:
            output_text_area.empty()
            frame_window.image([])
            cv2.waitKey(1)
            continue

        success, frame = capture.read()
        if not success:
            st.error("Failed to read from the camera.")
            break

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

        composed = cv2.addWeighted(frame, 0.7, canvas, 0.3, 0.0)
        frame_window.image(composed, channels="BGR")

        if latest_text:
            output_text_area.text(latest_text)

        cv2.waitKey(1)


if __name__ == "__main__":
    main()
