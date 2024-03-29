import json
import os
from json import JSONDecodeError
from pathvalidate import ValidationError, validate_filename


class Parser:
    def __init__(self, root_path: str, json_path: str):
        self.validate_params(root_path, json_path)
        self.root_path = root_path
        self.json_path = json_path
        if os.path.exists(root_path) and len(os.listdir(root_path)) != 0:
            Parser.warn_that_root_not_empty(root_path)
        self.dir_struct = dict()

    def get_json_dict_from_dir(self, dir_path, dir_struct=None):
        # root wasn't created yet (first recursion step)
        if dir_struct is None:
            dir_struct = dict()
            dir_struct[self.root_path.split("/")[-1]] = dict()
            self.dir_struct = dir_struct

        dir_name = dir_path.split("/")[-1]

        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)

            if os.path.isdir(item_path):
                item = item.split("/")[-1]
                dir_struct[dir_name][item] = dict()
                self.get_json_dict_from_dir(item_path, dir_struct[dir_name])
            else:
                file = open(item_path, "r")
                file_content = file.read()
                file.close()
                dir_struct[dir_name][item] = file_content
        return dir_struct

    @staticmethod
    def validate_params(root_path: str, json_path: str) -> None:
        if not os.path.isdir(root_path):
            raise Exception(f"The root directory path given '{root_path}' is not a valid path!")
        # if not os.path.isfile(json_path):
        #     raise Exception(f"The json file path given '{json_path}' is not a valid path!")

    @staticmethod
    def warn_that_root_not_empty(root_path: str) -> None:
        warning_message = f"[WARNING] The root directory {root_path} isn't empty."
        print(warning_message)
        while True:
            answer = input(f"-> Do you want to override the current structure: [yes|no]? ")
            if answer.lower() == "yes":
                print("[INFO] OK. The current structure will be overriden.\n")
                break
            if answer.lower() == "no":
                print("[INFO] As you requested, the current process will be now aborted... Bye!")
                exit()
            print("[WARNING] Please type 'yes', 'YES' or 'no', 'NO'!")

    @staticmethod
    def validate_item(item_name: str) -> None:
        try:
            validate_filename(item_name)
        except ValidationError as exception:
            # only extract the explanation of the error
            raise Exception(f"The name='{item_name}' isn't valid because: {str(exception).split(sep=',')[0]}")

    def validate_dir_structure(self, dir_structure: dict, root: str) -> None:
        for key in dir_structure.keys():
            Parser.validate_item(key)
            if type(dir_structure[key]) == dict:
                self.validate_dir_structure(dir_structure[key], os.path.join(root, key))

    def get_json_dict(self) -> dict:
        try:
            file = open(self.json_path, "r")
            dir_structure = json.loads(file.read())
            self.validate_dir_structure(dir_structure, self.root_path)
            file.close()
            return dir_structure
        except OSError:
            raise Exception(f"The json file '{self.json_path}' can't be opened!")
        except JSONDecodeError:
            raise Exception(f"The json file '{self.json_path}' isn't a valid json file!")
