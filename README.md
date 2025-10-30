<img src="assets/abner2.jpg" alt="Banner" style="width:100%; height:150px; object-fit:cover; object-position:center;" />

# Math Gesture Solver

Hands-free math tutoring experiment that uses a webcam, hand gestures, and Google Gemini to solve equations you “write” in the air. Built with Streamlit/OpenCV for the primary experience, plus a Tkinter desktop prototype and supporting learning materials.

## Features
- Real-time gesture-based drawing with `cvzone` and OpenCV overlays.
- Gemini 1.5 Flash integration to analyse the virtual whiteboard and return step-by-step math answers.
- Streamlit UI with live camera feed, banner branding, and answer panel.
- Tkinter fallback app (`maintk.py`) for environments where Streamlit is not desired.
- Companion notebooks covering core Python concepts for the MG Sulsel Koding curriculum.

## Project Layout
- `main.py`: Streamlit interface that captures gestures, renders the canvas, and queries Gemini.
- `maintk.py`: Desktop variant using Tkinter with the same gesture pipeline.
- `calculator.py`: Stand-alone basic calculator used in workshops.
- `notebooks/`: Jupyter notebooks (`input_output`, `variables_operators`, `conditions`, `looping`, `functions`, `data_structure`) introducing Python fundamentals.
- `assets/`: Branding images used by the Streamlit app (e.g., banner artwork).

## Getting Started
### Prerequisites
- Python 3.10+
- Webcam accessible at index `1` by default (update `CAMERA_INDEX` if needed).
- Google Gemini API key (`GOOGLE_API_KEY`) with access to the 1.5 Flash model.

### Setup
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install streamlit opencv-python cvzone google-generativeai pillow numpy
```

### Configure Credentials
- Environment variable: `export GOOGLE_API_KEY="your-key"`
- or Streamlit secrets: create `.streamlit/secrets.toml` with
  ```toml
  GOOGLE_API_KEY = "your-key"
  ```

## Usage
- Streamlit experience:
  ```bash
  streamlit run main.py
  ```
- Tkinter desktop prototype:
  ```bash
  python maintk.py
  ```
- Basic calculator demo:
  ```bash
  python calculator.py
  ```

## Gesture Reference
- `Draw` (`[0,1,0,0,0]`): Index finger up → writes on the virtual canvas.
- `Clear` (`[1,0,0,0,0]`): Thumb up → wipes the canvas clean.
- `Submit` (`[1,1,1,1,0]`): All fingers except pinky → sends the canvas to Gemini and displays the answer.

## Tips for Workshops
- Encourage participants to keep their hand within the frame for reliable gesture detection.
- Prepare fallback text prompts or screenshots if the network connection for Gemini is unstable.
- Use the notebooks as pre-work to introduce the Python concepts referenced in the app’s code.

## Troubleshooting
- Camera not found: Update `CAMERA_INDEX` in the scripts to match your device.
- Gemini errors: Ensure the API key is active and billing is enabled for generative models.
- Missing packages: Verify the virtual environment is activated before installing or running commands.

## License
Document the license here once confirmed (currently unspecified).
