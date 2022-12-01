import json
import os
from json import JSONDecodeError


class Parser:
    def __init__(self, root_path, json_path):
        self.validate_params(root_path, json_path)
        self.root_path = root_path
        self.json_path = json_path

    @staticmethod
    def validate_params(root_path, json_path):
        if not os.path.isdir(root_path):
            raise Exception(f"[ERROR] The root directory path given '{root_path}' is not a valid path!")
        if not os.path.isfile(json_path):
            raise Exception(f"[ERROR] The json file path given '{json_path}' is not a valid path!")

    @staticmethod
    def validate_dir_structure(dir_structure):
        pass

    def get_json_dict(self):
        try:
            file = open(self.json_path, "r")
            dir_structure = json.loads(file.read())
            self.validate_dir_structure(dir_structure)
            file.close()
            return dir_structure
        except OSError:
            raise Exception(f"[ERROR] The json file '{self.json_path}' can't be opened!")
        except JSONDecodeError:
            raise Exception(f"[ERROR] The json file '{self.json_path}' isn't a valid json file!")
