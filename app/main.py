from app.core.config import (
	APP_NAME,
	VIDEO_OUTPUT_PATH,
	VIDEO_SOURCE,
)
from app.detection.detector import TrafficDetector
from app.video.frame_processor import VideoProcessor


def main() -> None:
	print(f"=== {APP_NAME} ===")

	detector = TrafficDetector()

	print("Device information:", detector.get_device_info())
	print("YOLO detector initialized successfully.")

	processor = VideoProcessor(detector)
	processor.run(input_path=VIDEO_SOURCE, output_path=VIDEO_OUTPUT_PATH, show=False)

if __name__ == "__main__":
	main()