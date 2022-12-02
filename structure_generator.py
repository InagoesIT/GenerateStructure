import os

from parser import Parser
import shutil


class StructureGenerator:
    def __init__(self, root_path: str, json_path: str):
        self.parser = Parser(root_path, json_path)

    def run(self) -> None:
        dir_structure = self.parser.get_json_dict()
        StructureGenerator.create_or_delete_dir(self.parser.root_path)
        self.generate_structure(dir_structure, self.parser.root_path)

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
