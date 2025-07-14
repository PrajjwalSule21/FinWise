from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from pathlib import Path
import shutil
from utils.utils import remove_all_files_in_directory

router = APIRouter()

DATA_DIR = Path("data")

@router.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    allowed_extensions = (".csv", ".xlsx")
    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(status_code=400, detail="Only CSV and Excel files are allowed.")

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Assuming remove_existing_file is imported and accepts Path object as directory
    remove_all_files_in_directory(directory=DATA_DIR)

    file_path = DATA_DIR / file.filename

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"message": f"File '{file.filename}' uploaded successfully."}