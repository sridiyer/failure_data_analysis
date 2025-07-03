"""
Pickle file reader module for loading serialized Python objects.
"""

import pickle
from pathlib import Path
from typing import Any, Union


def read_pickle_file(file_path: Union[str, Path]) -> Any:
    """
    Read a pickle file and return the deserialized data.
    
    Args:
        file_path: Path to the pickle file (string or Path object)
        
    Returns:
        The deserialized data from the pickle file
        
    Raises:
        FileNotFoundError: If the pickle file doesn't exist
        pickle.UnpicklingError: If the pickle file is corrupted or invalid
        Exception: For other file reading errors
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Pickle file not found: {file_path}")
    
    if not file_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except pickle.UnpicklingError as e:
        raise pickle.UnpicklingError(f"Failed to unpickle file {file_path}: {e}")
    except Exception as e:
        raise Exception(f"Error reading pickle file {file_path}: {e}")


def read_pickle_file_safe(file_path: Union[str, Path], default: Any = None) -> Any:
    """
    Safely read a pickle file and return the deserialized data.
    Returns default value if file cannot be read.
    
    Args:
        file_path: Path to the pickle file (string or Path object)
        default: Default value to return if file cannot be read
        
    Returns:
        The deserialized data from the pickle file or default value
    """
    try:
        return read_pickle_file(file_path)
    except Exception:
        return default 