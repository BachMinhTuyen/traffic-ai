# Traffic AI

Traffic AI is an intelligent traffic monitoring and analysis system designed to detect, classify, and track objects from video streams and cameras.

The system focuses on real-time computer vision processing for traffic environments, including:

* 🚗 Vehicle detection and classification
* 🧑 Person detection
* 🎯 Multi-object tracking
* 🔢 Vehicle and person counting
* ↔️ Movement direction detection
* 🏎️ Vehicle speed estimation
* 📍 Detection zones and regions of interest
* 📹 Video file, webcam, and RTSP camera support
* 📡 Real-time AI data delivery through API and WebSocket
* 📊 Traffic statistics and monitoring dashboard

The core AI pipeline is built with **Python, OpenCV, PyTorch, and Ultralytics YOLO**, while **FastAPI** provides the backend API for integration with a web-based dashboard.

```text
Camera / Video
      │
      ▼
   OpenCV
      │
      ▼
 YOLO Detection
      │
      ▼
 Object Tracking
      │
      ▼
 Traffic Analytics
 ├── Counting
 ├── Direction
 ├── Speed
 └── Detection Zones
      │
      ▼
    FastAPI
 ├── REST API
 └── WebSocket
      │
      ▼
 Web Dashboard
```

---

# Requirements

## Recommended Environment

| Component     | Recommended                                     |
| ------------- | ----------------------------------------------- |
| OS            | Ubuntu 24.04 / Windows 10+                      |
| Python        | 3.12                                            |
| Git           | Latest stable                                   |
| FFmpeg        | Latest available                                |
| CPU           | 4+ cores                                        |
| RAM           | 8 GB+                                           |
| GPU           | NVIDIA GPU recommended for real-time processing |
| NVIDIA Driver | Required for GPU acceleration                   |

> GPU acceleration currently targets NVIDIA GPUs through CUDA-enabled PyTorch.

---

# Project Structure

```text
traffic-ai/
├── app/
│   ├── api/
│   ├── camera/
│   ├── detection/
│   ├── tracking/
│   ├── analytics/
│   └── core/
│
├── models/
├── scripts/
├── tests/
├── videos/
│
├── .env
├── .env.example
├── .gitignore
├── requirements/
│   ├── base.txt
│   ├── cpu.txt
│   └── gpu.txt
│
└── README.md
```

---

# Setup on Windows

## 1. Install prerequisites

Install the following applications:

* Python 3.12
* Git
* FFmpeg

Check the installation:

```powershell
python --version
git --version
ffmpeg -version
```

Expected Python version:

```text
Python 3.12.x
```

---

## 2. Clone the repository

```powershell
git clone <repository-url>
cd traffic-ai
```

---

## 3. Create Python virtual environment

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify:

```powershell
python --version
python -m pip --version
```

The pip path should point to:

```text
traffic-ai\.venv\
```

---

# Windows - CPU Setup

Upgrade Python packaging tools:

```powershell
python -m pip install --upgrade pip setuptools wheel
```

Install the base dependencies:

```powershell
python -m pip install -r requirements\base.txt
```

Install CPU PyTorch:

```powershell
python -m pip install torch torchvision torchaudio
```

Or, if `requirements\cpu.txt` contains the correct CPU dependencies:

```powershell
python -m pip install -r requirements\cpu.txt
```

---

# Windows - NVIDIA GPU Setup

## 1. Check NVIDIA GPU

Open PowerShell:

```powershell
nvidia-smi
```

Verify that the NVIDIA driver and GPU are detected.

Example:

```text
NVIDIA-SMI ...
GPU Name ...
Driver Version ...
CUDA Version ...
```

## 2. Install PyTorch

Install the CUDA-enabled PyTorch version appropriate for your NVIDIA driver from the official PyTorch installation instructions.

After installation, verify CUDA:

```powershell
python -c "import torch; print('PyTorch:', torch.__version__); print('CUDA:', torch.cuda.is_available())"
```

Expected:

```text
PyTorch: ...
CUDA: True
```

Check the GPU:

```powershell
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

Then install the remaining dependencies:

```powershell
python -m pip install -r requirements\base.txt
```

---

# Setup on Ubuntu

The recommended Linux development environment is:

```text
Ubuntu 24.04
Python 3.12
```

---

## 1. Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

Install system dependencies:

```bash
sudo apt install -y \
    python3 \
    python3-venv \
    python3-pip \
    python3-dev \
    build-essential \
    pkg-config \
    git \
    ffmpeg
```

Verify:

```bash
python3 --version
git --version
ffmpeg -version
```

Expected Python:

```text
Python 3.12.x
```

---

## 2. Clone the repository

```bash
git clone <repository-url>
cd traffic-ai
```

---

## 3. Create Python virtual environment

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Verify:

```bash
which python
which pip
```

Expected:

```text
/home/<user>/traffic-ai/.venv/bin/python
/home/<user>/traffic-ai/.venv/bin/pip
```

---

# Ubuntu - CPU Setup

Upgrade Python packaging tools:

```bash
python -m pip install --upgrade pip setuptools wheel
```

Install base dependencies:

```bash
python -m pip install -r requirements/base.txt
```

Install CPU PyTorch:

```bash
python -m pip install torch torchvision torchaudio
```

Or:

```bash
python -m pip install -r requirements/cpu.txt
```

---

# Ubuntu - NVIDIA GPU Setup

## 1. Check NVIDIA GPU

```bash
nvidia-smi
```

Verify:

* NVIDIA GPU is detected
* NVIDIA driver is installed
* CUDA compatibility is available

Do not install a random CUDA Toolkit version just because CUDA is required by PyTorch.

The PyTorch package normally provides the required CUDA runtime components for its supported build. The NVIDIA driver must still be installed correctly.

## 2. Install PyTorch

Install the CUDA-enabled PyTorch version appropriate for your GPU/driver combination.

Then verify:

```bash
python - <<'PY'
import torch

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("CUDA version:", torch.version.cuda)
    print("GPU:", torch.cuda.get_device_name(0))
PY
```

Expected:

```text
PyTorch: ...
CUDA available: True
CUDA version: ...
GPU: NVIDIA ...
```

Then install the base dependencies:

```bash
python -m pip install -r requirements/base.txt
```

---

# Python Dependencies

The project separates common dependencies from CPU/GPU-specific dependencies.

```text
requirements/
├── base.txt
├── cpu.txt
└── gpu.txt
```

## Base dependencies

The base environment contains:

```text
NumPy
OpenCV
Ultralytics
FastAPI
Uvicorn
```

Install:

```bash
python -m pip install -r requirements/base.txt
```

## CPU dependencies

CPU environments additionally require CPU-compatible PyTorch:

```bash
python -m pip install -r requirements/cpu.txt
```

## GPU dependencies

GPU environments require a CUDA-enabled PyTorch build:

```bash
python -m pip install -r requirements/gpu.txt
```

> The PyTorch version in `gpu.txt` should match the CUDA/PyTorch configuration supported by the target NVIDIA environment.

---

# Verify Installation

After activating `.venv`, run:

```bash
python - <<'PY'
import cv2
import numpy
import torch
import fastapi
import ultralytics

print("=== Traffic AI Environment ===")
print("NumPy:       ", numpy.__version__)
print("OpenCV:      ", cv2.__version__)
print("PyTorch:     ", torch.__version__)
print("FastAPI:     ", fastapi.__version__)
print("Ultralytics: ", ultralytics.__version__)
print("CUDA:        ", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:         ", torch.cuda.get_device_name(0))
PY
```

Example CPU result:

```text
=== Traffic AI Environment ===
NumPy:        ...
OpenCV:       ...
PyTorch:      ...
FastAPI:      ...
Ultralytics:  ...
CUDA:         False
```

Example GPU result:

```text
=== Traffic AI Environment ===
NumPy:        ...
OpenCV:       ...
PyTorch:      ...
FastAPI:      ...
Ultralytics:  ...
CUDA:         True
GPU:          NVIDIA ...
```

---

# Test YOLO

Run:

```bash
python - <<'PY'
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model("https://ultralytics.com/images/bus.jpg")

print("YOLO inference: OK")
PY
```

For GPU:

```bash
python - <<'PY'
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model(
    "https://ultralytics.com/images/bus.jpg",
    device=0
)

print("YOLO GPU inference: OK")
PY
```

---

# FFmpeg

FFmpeg is a system-level dependency and should **not** be installed inside `.venv`.

Ubuntu:

```bash
sudo apt install -y ffmpeg
```

Windows:

Install FFmpeg and make sure the `ffmpeg` command is available in `PATH`.

Verify:

```bash
ffmpeg -version
```

FFmpeg is used for:

* Video decoding
* Video encoding
* RTSP streams
* H.264/H.265
* Video conversion
* Video processing

The Python environment can use FFmpeg through OpenCV or other Python libraries.

---

# Virtual Environment

The project uses Python virtual environments to prevent global Python packages from interfering with the project.

```text
traffic-ai/
└── .venv/
    ├── pip
    ├── setuptools
    ├── wheel
    ├── numpy
    ├── opencv-python
    ├── torch
    ├── torchvision
    ├── torchaudio
    ├── ultralytics
    ├── fastapi
    └── uvicorn
```

Never commit `.venv` to Git.

`.gitignore` should contain:

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
models/*.pt
models/*.onnx
models/*.engine
videos/
outputs/
```

---

# Activate / Deactivate Environment

## Ubuntu

Activate:

```bash
source .venv/bin/activate
```

Deactivate:

```bash
deactivate
```

## Windows PowerShell

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

Deactivate:

```powershell
deactivate
```

---

# Reinstall Dependencies

If the virtual environment is corrupted, remove it and create a new one.

Ubuntu:

```bash
rm -rf .venv

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip setuptools wheel
```

Windows:

```powershell
Remove-Item -Recurse -Force .venv

python -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip setuptools wheel
```

Then install the appropriate CPU/GPU dependencies again.

---

# Development Workflow

The recommended development process is:

```text
1. Object Detection
        ↓
2. Object Classification
        ↓
3. Object Tracking
        ↓
4. Track ID
        ↓
5. Counting
        ↓
6. Direction Detection
        ↓
7. Speed Estimation
        ↓
8. Detection Zones
        ↓
9. RTSP Camera
        ↓
10. FastAPI
        ↓
11. WebSocket
        ↓
12. Web Dashboard
```

The AI processing should remain in the Python service.

The web application should consume AI results through REST API/WebSocket rather than performing YOLO inference directly in the browser.

---

# Architecture

```text
                   ┌───────────────┐
                   │ IP Camera     │
                   │ RTSP / Video  │
                   └───────┬───────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   OpenCV    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │    YOLO     │
                    │ Detection   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Tracker   │
                    │ ByteTrack / │
                    │  BoT-SORT   │
                    └──────┬──────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Traffic         │
                  │ Analytics       │
                  ├─────────────────┤
                  │ Counting        │
                  │ Direction       │
                  │ Speed           │
                  │ Zones           │
                  └────────┬────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    ├─────────────┤
                    │ REST API    │
                    │ WebSocket   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Web Client  │
                    │   Next.js   │
                    └─────────────┘
```

---

# CPU vs GPU

## CPU

Suitable for:

* Development
* Unit tests
* Video processing
* Algorithm development
* API development
* Low-volume inference
* Debugging

```text
CPU
 ↓
OpenCV
 ↓
YOLO
 ↓
Tracking
```

## NVIDIA GPU

Recommended for:

* Real-time inference
* High-resolution video
* Multiple cameras
* Multiple objects
* High FPS
* Model training/fine-tuning

```text
NVIDIA GPU
 ↓
CUDA
 ↓
PyTorch
 ↓
YOLO
 ↓
Tracking
```

For production traffic monitoring, an NVIDIA GPU is recommended when processing multiple RTSP cameras simultaneously.

---

# Notes

* Do not install Python project dependencies globally.
* Always activate `.venv` before installing Python packages.
* Use `python -m pip` instead of a global `pip` command when possible.
* FFmpeg is installed at the system level, not inside `.venv`.
* NVIDIA Driver is installed at the system level, not inside `.venv`.
* PyTorch is installed inside `.venv`.
* Do not commit `.venv` to Git.
* Do not commit large model files unless explicitly required.
* GPU environments require a compatible NVIDIA driver and CUDA-enabled PyTorch build.
* The same source code should be able to run on both CPU and GPU environments.

---

# License

This project is currently a personal project and does not have a finalized open-source license yet.

The license terms will be updated once the project license is officially decided.
Until then, please consider the source code as **unlicensed** and do not assume that it is permitted to copy, modify, redistribute, or use commercially without permission from the author.
