# Real-Time Object Detection with YOLOv8 and OpenCV

A Python application that detects objects in real time from a webcam or video file using [Ultralytics YOLOv8](https://docs.ultralytics.com/) and OpenCV. Each detected object is outlined with a bounding box, marked with a center point, and labeled with its class name (from the 80 COCO classes).

## Features

- Real-time detection from a webcam or a video file
- Pretrained YOLOv8 model (`yolov8s.pt`) that recognizes the 80 COCO object classes
- Bounding boxes, center-point markers, and readable labels (outlined text) drawn on each frame
- Configurable frame skipping for slower machines
- Press `Esc` to quit

## Tech Stack

- Python 3.8+
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV (`opencv-python`)
- pandas

## Project Structure

```
object-detection/
├── main.py            # Main detection script (rename to match your file)
├── coco.txt           # COCO class names, one per line
├── requirements.txt   # Python dependencies
├── yolov8s.pt         # YOLOv8 small weights (auto-downloaded on first run)
└── README.md
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<VishantJawandha>/<Object-Detection-Model>.git
   cd <your-repo-name>
   ```

2. **Create and activate a virtual environment (recommended)**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make sure `coco.txt` is present** in the project root. It should contain the 80 COCO class names, one per line (`person`, `bicycle`, `car`, ...).

The YOLOv8 weights (`yolov8s.pt`) download automatically the first time you run the script.

## Usage

Run the script:

```bash
python main.py
```

### Choose your input source

In the script, set `video_src`:

```python
video_src = 0              # default webcam
# video_src = "video2.mp4" # or a video file
```

### Windows webcam note

The script opens the camera with the Media Foundation backend:

```python
cap = cv2.VideoCapture(video_src, cv2.CAP_MSMF)
```

`cv2.CAP_MSMF` is **Windows only**. On Linux or macOS, remove the second argument:

```python
cap = cv2.VideoCapture(video_src)
```

### Controls

| Key   | Action              |
|-------|---------------------|
| `Esc` | Close the window and exit |

## How It Works

1. A frame is read from the webcam or video file.
2. The frame is passed to YOLOv8, which returns bounding boxes, confidence scores, and class IDs.
3. For each detection, the script maps the class ID to a name using `coco.txt`.
4. A rectangle, center dot, and label are drawn on a copy of the frame.
5. The annotated frame is shown in an OpenCV window.

## Configuration

| Setting          | Where                 | Description |
|------------------|-----------------------|-------------|
| `video_src`      | Main script           | `0` for webcam, or a path to a video file |
| `frames_to_skip` | Main script           | Frames to skip between detections; increase for better speed on slow hardware |
| Model weights    | `YOLO('yolov8s.pt')`  | Swap for `yolov8n.pt` (faster), `yolov8m.pt`, or `yolov8l.pt` (more accurate) |

## Requirements

Create a `requirements.txt` with:

```
ultralytics
opencv-python
pandas
```

## Troubleshooting

- **Webcam doesn't open:** Try a different index (`1`, `2`), close other apps using the camera, or remove `cv2.CAP_MSMF` if you're not on Windows.
- **`FileNotFoundError: coco.txt`:** Run the script from the project folder, or make sure `coco.txt` is next to it.
- **Low FPS:** Use `yolov8n.pt`, increase `frames_to_skip`, or run on a machine with a GPU (install a CUDA-enabled build of PyTorch).
- **`cv2.imshow` errors on a server:** Servers without a display can't open windows. Use a local machine, or see the deployment notes below.

## Deployment Notes

This script uses `cv2.imshow` and a local webcam, so it runs as a desktop app. To deploy it online, you have a few options:

- **Web app with Streamlit or Gradio:** Wrap `findObject()` in a UI that accepts an image, video upload, or browser webcam stream. Both can be hosted on Streamlit Community Cloud or Hugging Face Spaces.
- **REST API with FastAPI or Flask:** Expose an endpoint that accepts an image and returns the annotated image or JSON detections, then containerize it with Docker.
- **Docker:** Package the app and dependencies in a container for consistent deployment to AWS (EC2, ECS) or any cloud host.

## Future Improvements

- Confidence threshold and class filtering
- Image and batch-folder mode
- FPS counter overlay
- Object tracking across frames
- Web interface for browser-based demos

## Acknowledgements

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8
- [COCO Dataset](https://cocodataset.org/) for the class labels
- [OpenCV](https://opencv.org/)

## License

This project is licensed under the MIT License. Add a `LICENSE` file to your repository to match.

## Author

**Vishant**
GitHub: [@VishantJawandha](https://github.com/VishantJawandha)