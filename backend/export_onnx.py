from ultralytics import YOLO
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

models_folder = ROOT / "models"
models_folder.mkdir(exist_ok=True)

print("Loading YOLO model...")

model = YOLO("yolo11n.pt")

print("Exporting to ONNX...")

model.export(
    format="onnx",
    imgsz=640,
    opset=17,
    simplify=True
)

print("\nModel exported successfully!")