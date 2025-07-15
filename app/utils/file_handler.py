import os
from pathlib import Path
import pandas as pd

def remove_all_files_in_directory(directory: str) -> int:
    """
    Deletes all files in the specified directory.

    Args:
        directory (str): The directory path where files will be deleted.

    Returns:
        int: The number of files deleted.
    """
    dir_path = Path(directory)
    deleted_count = 0

    if not dir_path.exists() or not dir_path.is_dir():
        return deleted_count  

    for file_path in dir_path.iterdir():
        if file_path.is_file():
            try:
                os.remove(file_path)
                deleted_count += 1
            except Exception as e:
                pass

    return deleted_count



def read_file_as_string(directory: str) -> str:
    """
    Reads the first CSV or Excel file in the directory and returns its content as a string.

    Args:
        directory (str): Path to the folder where the file is located.

    Returns:
        str: File content as a string suitable for LLM input.
    """
    dir_path = Path(directory)

    if not dir_path.exists() or not dir_path.is_dir():
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    supported_files = list(dir_path.glob("*.csv")) + list(dir_path.glob("*.xlsx"))
    if not supported_files:
        raise FileNotFoundError("No CSV or Excel file found in the directory.")

    file_path = supported_files[0]  

    if file_path.suffix == ".csv":
        df = pd.read_csv(file_path)
    elif file_path.suffix == ".xlsx":
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format.")

    return df.to_string(index=False)