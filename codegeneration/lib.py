import os
import shutil
from functools import reduce

from config import config


def read_txt_file(file_name):
    assert os.path.isfile(file_name), f"'{file_name}' - file not found"
    return open(file_name, encoding='utf8').read().strip()

def apply_color_tags_in_text(text):
    result = reduce(lambda reduced, next: reduced.replace(*next), list(config('COLOR_TAGS').items()), text)
    assert 'C_' not in result, f"not all color tag can be applied:\n{result}"
    return result

def write_txt_file(file_name, content):
    with open(file_name, 'w', encoding='utf8') as text_file:
        text_file.write(content)

def append_to_txt_file(file_name, content):
    with open(file_name, 'a', encoding='utf8') as text_file:
        text_file.write(content)

def hl():
    terminal_width = shutil.get_terminal_size().columns
    return f"[bright_black]{'·' * terminal_width}[/]"
