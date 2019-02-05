import os

def ensure_path(path):
    os.makedirs(path, exist_ok=True)
