import torch
from ultralytics import YOLO

from app.core.config import (
	AI_CONFIDENCE,
	AI_DEVICE,
	DETECTION_CLASSES,
	MODEL_PATH,
)


class TrafficDetector:
	def __init__(self) -> None:
		if not MODEL_PATH.exists():
			raise FileNotFoundError(
				f"YOLO model not found: {MODEL_PATH}"
			)

		self.device = (
			0 if AI_DEVICE.isdigit() else AI_DEVICE
		)

		self.model = YOLO(str(MODEL_PATH))

	def detect(self, frame):
		return self.model.predict(
			source=frame,
			device=self.device,
			conf=AI_CONFIDENCE,
			classes=DETECTION_CLASSES,
			verbose=False,
		)

	@staticmethod
	def get_device_info() -> dict:
		return {
			"cuda_available": torch.cuda.is_available(),
			"gpu_name": (
				torch.cuda.get_device_name(0)
				if torch.cuda.is_available()
				else None
			),
		}