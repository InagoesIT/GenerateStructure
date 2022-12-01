import json
import os
from json import JSONDecodeError


def validate_dir_structure():
    pass


class Parser:
    def __init__(self, root_path, json_path):
        self.validate_params(root_path, json_path)
        self.root_path = root_path
        self.json_path = json_path

    @staticmethod
    def validate_params(root_path, json_path):
        if not os.path.isdir(root_path):
            raise OSError(f"[ERROR] The root directory path given '{root_path}' is not a valid path!")
        if not os.path.isfile(json_path):
            raise FileNotFoundError(f"[ERROR] The json file path given '{json_path}' is not a valid path!")




