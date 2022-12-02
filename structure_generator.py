from parser import Parser


class StructureGenerator:
    def __init__(self, root_path: str, json_path: str):
        self.parser = Parser(root_path, json_path)
        self.root_path = root_path
        self.json_path = json_path

    def run(self) -> None:
        dir_structure = self.parser.get_json_dict()
