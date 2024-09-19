# Hand Detection and Matrix Rain Animation

This project combines **hand detection** using [MediaPipe](https://google.github.io/mediapipe/) and a cool **Matrix rain animation** using [Pygame](https://www.pygame.org/) to create an interactive experience. The application detects **hand gestures** through a webcam and displays an animation of falling `0` and `1` once both hands show a "like" gesture 👍.

## Features
- **Real-time hand gesture detection**: Uses MediaPipe to track and detect hand landmarks.
- **Like gesture recognition**: Detects when both hands make a "like" (thumbs up) gesture.
- **Matrix-style animation**: After detecting the like gesture, it triggers a matrix-style rain animation with falling `0` and `1`.
- **Fun visualization**: Displays the live camera feed along with detected hand landmarks.

## How It Works
1. The program captures the video feed from your webcam and uses MediaPipe to detect hands.
2. It looks for a "like" gesture in each detected hand.
3. Once the like gesture is detected in both hands, the animation of falling binary numbers (inspired by the Matrix movie) starts.
4. Press **'q'** to exit the application.

## Installation
To run this project, you'll need Python 3 and the following libraries:
- OpenCV: `pip install opencv-python`
- MediaPipe: `pip install mediapipe`
- Pygame: `pip install pygame`
- Install all dependencies:
  ```bash
  pip install opencv-python mediapipe pygame
  ```

## Usage

1. Clone the repository:
  ```bash
  git clone https://github.com/faezedrx/hand-detection-matrix-rain.git
  cd hand-detection-matrix-rain
  ```
2. Run the script:
  ```bash
  python main.py
  ```
3. Show a "like" gesture using both hands and enjoy the animation!
