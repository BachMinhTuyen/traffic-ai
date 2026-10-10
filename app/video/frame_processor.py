from pathlib import Path

import cv2

from app.detection.detector import TrafficDetector
from app.video.sources import VideoSource

class VideoProcessor:
	def __init__(self, detector:TrafficDetector) -> None:
		self.detector = detector

	def run(self,
			input_path: str | Path,
			output_path: str | Path,
			show: bool = True
		) -> None:
		output_path = Path(output_path)
		output_path.parent.mkdir(parents=True, exist_ok=True)

		source = VideoSource(input_path)
		writer = None
		window_name = "Traffic AI - YOLO Detection"
		frame_count = 0

		try:
			source.open()

			fps = source.fps
			if fps <= 0:
				fps = 25

			width = source.width
			height = source.height

			if width <= 0 or height <=0:
				raise RuntimeError(
					"Unable to determine input videp dimensions."
				)

			fourcc = cv2.VideoWriter.fourcc(*"mp4v")
			writer = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))

			if not writer.isOpened():
				raise RuntimeError(
					f"Cannot create output video: {output_path}"
				)

			if show:
				cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

			print(f"Input: {input_path}")
			print(f"Output: {output_path}")
			print(f"Resolution: {width}x{height}")
			print(f"FPS: {fps:.2f}")
			print("Press 'q' to stop processing.")

			while True:
				success, frame = source.read()

				if not success:
					break

				results = self.detector.detect(frame)
				annotated_frame = results[0].plot()

				# Save the annotated frame
				writer.write(annotated_frame)
				frame_count += 1

				if show:
					cv2.imshow(window_name, annotated_frame)

					if cv2.waitKey(1) & 0xFF == ord("q"):
						print("Stopped by user.")
						break

				if frame_count % 100 == 0:
					print(f"Processed {frame_count} frames")

			print(f"Total processed frames: {frame_count}")
			print(f"Output saved to: {output_path}")

		finally:
			source.release()

			if writer is not None:
				writer.release()

			if show:
				cv2.destroyAllWindows()