import os


def get_txt_file_content(file_name):
    assert os.path.isfile(file_name), f"'{file_name}' - file not found"
    return open(file_name).read().strip()
