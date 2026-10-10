from pathlib import Path
import cv2

class VideoSource:
	def __init__(self, source: str | Path):
		self.source = str(source)
		self.capture = None

	def open(self) -> "VideoSource":
		path = Path(self.source)

		if not path.exists():
			raise FileNotFoundError(
				f"Video source not found: {path}"
			)

		self.capture = cv2.VideoCapture(self.source)

		if not self.capture.isOpened():
			self.release()
			raise RuntimeError(
				f"Cannot open video source: {self.source}"
			)

		return self


	@property
	def fps(self) -> float:
		if self.capture is None:
			return 0.0
		return self.capture.get(cv2.CAP_PROP_FPS)

	@property
	def width(self) -> int:
		if self.capture is None:
			return 0
		return int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))

	@property
	def height(self) -> int:
		if self.capture is None:
			return 0
		return int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

	def read(self):
		if self.capture is None:
			raise RuntimeError("Video source has not been opened")
		return self.capture.read()

	def release(self) -> None:
		if self.capture is not None:
			self.capture.release()
			self.capture = None