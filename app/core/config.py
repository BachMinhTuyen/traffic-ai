import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(ROOT_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "Traffic AI")
AI_DEVICE = os.getenv("AI_DEVICE", "0")
AI_CONFIDENCE = float(os.getenv("AI_CONFIDENCE", "0.5"))

MODEL_PATH = Path(
	os.getenv("YOLO_MODEL", "models/yolo26n.pt")
)

if not MODEL_PATH.is_absolute():
	MODEL_PATH = ROOT_DIR / MODEL_PATH

VIDEO_OUTPUT_DIR = ROOT_DIR / os.getenv(
	"VIDEO_OUTPUT_DIR", "outputs"
)

VIDEO_SOURCE = Path(
	os.getenv("VIDEO_SOURCE", "videos/traffic.mp4")
)
if not VIDEO_SOURCE.is_absolute():
	VIDEO_SOURCE = ROOT_DIR / VIDEO_SOURCE

VIDEO_OUTPUT_DIR = Path(
	os.getenv("VIDEO_OUTPUT_DIR", "outputs")
)
if not VIDEO_OUTPUT_DIR.is_absolute():
	VIDEO_OUTPUT_DIR = ROOT_DIR / VIDEO_OUTPUT_DIR

VIDEO_OUTPUT_PATH = VIDEO_OUTPUT_DIR / "traffic_detected.mp4"

# COCO classes:
# 0 = person, 2 = car, 3 = motorcycle, 5 = bus, 7 = truck
DETECTION_CLASSES = [0, 2, 3, 5, 7]