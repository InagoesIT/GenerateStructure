import json
import os
import re

from parser import Parser
import shutil


class StructureGenerator:
    def __init__(self, root_path: str, json_path: str):
        self.parser = Parser(root_path, json_path)

    def run(self) -> None:
        dir_structure = self.parser.get_json_dict()
        StructureGenerator.create_or_delete_dir(self.parser.root_path)
        self.generate_structure(dir_structure, self.parser.root_path)
        self.pretty_print_structure(dir_structure)

    @staticmethod
    def generate_structure(dir_structure, root):
        for key in dir_structure.keys():
            key_path = os.path.join(root, key)
            if type(dir_structure[key]) == dict:
                StructureGenerator.create_or_delete_dir(key_path)
                StructureGenerator.generate_structure(dir_structure[key], key_path)
                continue
            file = open(key_path, mode="w")
            file.write(dir_structure[key])
            file.close()

    @staticmethod
    def create_or_delete_dir(dir_path):
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            try:
                shutil.rmtree(dir_path)
                os.mkdir(dir_path)
            except OSError as e:
                print(f"Could not delete {dir_path}, because: {e.strerror}")

    def pretty_print_structure(self, dir_structure: dict) -> None:
        print("~~~The generated structure:~~~")
        print(self.parser.root_path)

        result = json.dumps(dir_structure, indent="---")
        replacements = [
            (r'\{|\}|"|,', ""),  # delete { } " and ,
            (r'-+\n', ""),  # delete empty lines with -
            (r':\s+(?=-)', "\n")  # replace :\n+ with \n
        ]
        for old, new in replacements:
            result = re.sub(old, new, result)
        print(result.strip())
