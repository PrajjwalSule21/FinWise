import os
from pathlib import Path

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
        return deleted_count  # Directory doesn't exist or not a dir

    for file_path in dir_path.iterdir():
        if file_path.is_file():
            try:
                os.remove(file_path)
                deleted_count += 1
            except Exception as e:
                # Optionally log or handle errors here
                pass

    return deleted_count
