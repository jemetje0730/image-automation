from fastapi import APIRouter, UploadFile, File, HTTPException
from services.file_utils import save_uploaded_file

router = APIRouter()

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    filename = await save_uploaded_file(file)
    return {"filename": filename}
