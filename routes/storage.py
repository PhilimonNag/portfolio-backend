from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path
from fastapi.responses import FileResponse
import shutil
import uuid
from models import FileInfo
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

router=APIRouter()

@router.post("/upload/", response_model=FileInfo)
async def upload_file(file: UploadFile = File(...)):
    # Generate a unique filename using UUID
    file_extension = file.filename.split(".")[-1]  # Get original file extension
    unique_filename = f"{uuid.uuid4()}.{file_extension}"  # Create unique filename with extension
    file_location = UPLOAD_DIR / unique_filename
    
    # Save file to the uploads directory
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": unique_filename,
        "file_url": f"/files/{unique_filename}"
    }

@router.get("/files/{filename}", response_class=FileResponse)
async def get_file(filename: str):
    file_location = UPLOAD_DIR / filename
    if not file_location.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return file_location

