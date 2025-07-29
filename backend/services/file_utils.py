import os
from fastapi import UploadFile

UPLOAD_DIR = "assets"

async def save_uploaded_file(file: UploadFile) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    return file.filename

def get_asset_path(filename: str):
    full_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(full_path):
        return UPLOAD_DIR, filename
    return None, None