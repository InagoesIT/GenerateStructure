import sys

from structure_generator import StructureGenerator

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"[ERROR] There must be exactly 2 command line arguments but you gave {len(sys.argv) - 1}!")
    else:
        try:
            structure_generator = StructureGenerator(sys.argv[1], sys.argv[2])
            structure_generator.run()
        except Exception as exception:
            print(exception)

