import time
from ultralytics import YOLO
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

image = ROOT / "assets" / "Images" / "street.jpg"

print("Loading ONNX model...")

model = YOLO(ROOT / "models" / "yolo11n.onnx")

start = time.time()

model(str(image))

end = time.time()

print("--------------------------------")

print("Inference Time")

print(f"{end-start:.4f} seconds")

print("--------------------------------")