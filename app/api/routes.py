from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from pathlib import Path
import shutil

router = APIRouter()

DATA_DIR = Path("data")

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv") or file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = DATA_DIR / file.filename

    # Save the uploaded file
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"message": f"File '{file.filename}' uploaded successfully."}
