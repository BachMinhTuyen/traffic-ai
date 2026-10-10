from app.detection.detector import TrafficDetector


def main() -> None:
	detector = TrafficDetector()

	print("Traffic AI")
	print(detector.get_device_info())
	print("Detector initialized successfully.")


if __name__ == "__main__":
	main()