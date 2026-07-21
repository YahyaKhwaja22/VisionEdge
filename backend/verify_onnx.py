import onnx
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

model_path = ROOT / "models" / "yolo11n.onnx"

print("Loading ONNX model...")

model = onnx.load(str(model_path))

onnx.checker.check_model(model)

print("--------------------------------")

print("ONNX Model Verified Successfully")

print("--------------------------------")