from functools import reduce
import shutil
from rich import print
from rich.console import Console
import openai

import lib
from config import config


console = Console()
prompt = None

help_text = reduce(lambda reduced, next: reduced.replace(*next), [
    ('_C_HEAD', 'spring_green1'),
    ('_C_KEY', 'deep_sky_blue1'),
    ('_C_TEXT', 'light_slate_blue'),
    ('_C_PUNCT', 'grey53'),
], lib.get_txt_file_content(config('HELP_FILE_NAME')))


def rich_pformat(rich_string, highlight = False):
    with console.capture() as capture:
        console.print(rich_string, highlight=highlight)
    return capture.get()[:-1]

def get_prompt():
    return rich_pformat(f"{prompt or '[sky_blue3]+[/]'} ")

def set_prompt(prompt_str):
    global prompt
    prompt = prompt_str

def print_response(response):
    terminal_width = shutil.get_terminal_size().columns
    hl_dotted = f"[bright_black]{'·' * terminal_width}[/]"
    texts = list(map(lambda c: c['text'].strip(), response['choices']))
    if len(texts) == 1:
        print(texts[0])
    else:
        print(hl_dotted)
        print(hl_dotted.join(texts))
        print(hl_dotted)

def make_openai_api_request(aiprompt):
    assert len(aiprompt) > 0, "give a prompt to the transformer"
    openai.api_key = lib.get_txt_file_content(config('OPENAI_API_KEY_FILE_NAME'))
    response = openai.Completion.create(model="text-davinci-003", prompt=aiprompt, temperature=0, max_tokens=1000)
    print_response(response)
