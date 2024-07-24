# Face Mesh Controlled Cursor

This project uses OpenCV and MediaPipe to control the cursor with face movements and eye blinks. By leveraging MediaPipe's Face Mesh for precise facial landmark detection, this script maps specific face points to screen coordinates, allowing for intuitive cursor control and click actions.

## Features:
- **Face Tracking:** Uses MediaPipe Face Mesh to track facial landmarks.
- **Cursor Control:** Moves the cursor based on facial landmark positions.
- **Click Action:** Simulates a mouse click when specific facial gestures are detected (e.g., eye blinks).

## How It Works:
1. **Face Detection:** The script captures video from the webcam and processes each frame to detect face landmarks.
2. **Landmark Mapping:** It identifies key landmarks around the eyes and maps them to screen coordinates.
3. **Cursor Movement:** The cursor is moved to the corresponding screen position of the landmarks.
4. **Click Detection:** If the vertical distance between specific eye landmarks is small enough (indicating a blink), a mouse click is simulated.

## Dependencies:
- OpenCV
- MediaPipe
- PyAutoGUI

## Usage:
1. Ensure you have a webcam connected to your system.
2. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe pyautogui
3. Run the script:
   ```bash
   python FaceMeshMouse.py
