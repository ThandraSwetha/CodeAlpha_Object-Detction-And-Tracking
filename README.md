# Object Tracking Project

## Overview

This repository contains a simple object detection and tracking project built around YOLOv8 detection models. The project demonstrates running object detection on images or video and assigning persistent IDs to detected objects across frames using a tracking module. The repository includes example YOLOv8 weights (`yolov8n.pt`, `yolov8s.pt`) and a `main.py` runner to start detection and tracking.

## Features

- Real-time object detection using YOLOv8 models
- Frame-to-frame object tracking with stable IDs
- Support for image and video input (live webcam or file)

## Repository Contents

- `main.py`  — Main script to run detection and tracking.
- `yolov8n.pt`, `yolov8s.pt` — Example YOLOv8 model weight files (small and nano variants).
- `README.md` — This file.
- `requirements.txt` — Python dependencies.

## Requirements

- Python 3.8+
- A suitable PyTorch build for your platform and CUDA version (or CPU-only). See https://pytorch.org/get-started/locally/ for install instructions.
- pip

Recommended Python packages (see `requirements.txt`).

Note: Installing `torch` via `pip install -r requirements.txt` may not select the best CUDA-enabled wheel for your system. If you need GPU acceleration, follow the PyTorch install instructions and then install the remaining requirements.

## Installation

1. Create and activate a virtual environment (Windows example):

```powershell
python -m venv venv
& .\venv\Scripts\Activate.ps1
```

2. Install PyTorch (optional GPU) following the official guide, for example:

```powershell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

3. Install the remaining Python packages:

```powershell
pip install -r requirements.txt
```

## Usage

Run the main script to start detection and tracking. Typical usage:

```powershell
python main.py --source 0
```

Common `--source` values:
- `0` — Open webcam
- `path/to/video.mp4` — Video file
- `path/to/image.jpg` — Single image

If `main.py` supports model selection via arguments, pass the path to a weights file, e.g.:

```powershell
python main.py --weights yolov8s.pt --source 0
```

Outputs:
- A display window showing detections and track IDs
- Optionally saved annotated video or images if `main.py` implements saving

## How It Works (High Level)

1. YOLOv8 model processes each frame and returns bounding boxes, class IDs, and confidence scores.
2. A tracking module associates detections across frames to produce persistent track IDs. Typical trackers use motion and appearance cues to match detections frame-to-frame.
3. The script overlays bounding boxes and object IDs on frames and shows/saves the result.

For implementation specifics, review `main.py` to see which tracker is used and which command-line options are supported.

## Troubleshooting

- If the camera doesn't open, ensure no other application is using it and try a different index (0, 1, ...).
- If detection is slow, use a smaller model like `yolov8n.pt` (nano) or enable a GPU-enabled PyTorch build.
- If `torch` fails to install via `requirements.txt`, install `torch` separately following the official instructions and then re-run `pip install -r requirements.txt`.

## Contributing

Feel free to open issues or pull requests. Useful contributions include:

- Adding clearer CLI help and argument parsing
- Adding saving options for annotated outputs
- Integrating or documenting the specific tracker used

