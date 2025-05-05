import json
import os


def load_layout(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Layout file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
