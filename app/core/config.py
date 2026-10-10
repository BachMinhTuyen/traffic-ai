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