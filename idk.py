import os


def get_all_files_recursively(dir_path):
    all_files = list()
    for item in os.listdir(dir_path):
        item_path = f"{dir_path}/{item}"
        if os.path.isdir(item_path):
            all_files += get_all_files_recursively(item_path)
        else:
            all_files.append(item_path)
    return all_files
