from ultralytics import YOLO
from pathlib import Path

# Project root directory
ROOT = Path(__file__).resolve().parent.parent

# Image path
image_path = ROOT / "assets" / "Images" / "street.jpg"

print(f"Loading image from: {image_path}")

# Load YOLO11 Nano model
model = YOLO("yolo11n.pt")

# Run inference
results = model(str(image_path), save=True)

print("Inference completed successfully!")
print("Output image saved automatically.")