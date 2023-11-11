import os
import sys
import yaml
import base64

from exception import AppException
from logger import logging
import tensorflow as tf
from constant.application import gender_dict

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a Python dictionary.

    Args:
        file_path (str): The path to the YAML file to be read.

    Returns:
        dict: A dictionary containing the contents of the YAML file.

    Raises:
        AppException: If any error occurs during file reading or parsing, this exception is raised.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Writes a Python object to a YAML file.

    Args:
        file_path (str): The path to the YAML file to be written.
        content (object): The Python object to be written to the YAML file.
        replace (bool, optional): If True, it will replace the existing file, if it exists. Default is False.

    Raises:
        AppException: If any error occurs during file writing, this exception is raised.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write yaml file")
    except Exception as e:
        raise AppException(e, sys)

def decodeImage(imgString, filename):
    """
    Decodes a base64-encoded image string and saves it as a binary file.

    Args:
        imgString (str): The base64-encoded image string.
        filename (str): The name of the file to save the decoded image.

    Returns:
        None

    Saves the decoded image as a binary file in the "./data/" directory.
    """
    imgdata = base64.b64decode(imgString)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    """
    Encodes an image file into a base64-encoded string.

    Args:
        croppedImagePath (str): The path to the image file to be encoded.

    Returns:
        str: The base64-encoded image as a string.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

