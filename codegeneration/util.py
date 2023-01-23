import os
import shutil
from rich import print as richprint
from rich.console import Console
import openai

import lib
from config import config


console = Console()
prompt = None

help_text = lib.apply_color_tags_in_text(lib.get_txt_file_content(config('HELP_FILE_NAME')))

api_key_not_found_text = lib.apply_color_tags_in_text('''
[C_HEAD]OpanAI API key not found[/]
[C_TEXT]Go to [C_LINK]https://beta.openai.com/[/] [C_PUNCT]>[/][C_TEXT] create an account [C_PUNCT]>[/][C_TEXT] Profile menu [C_PUNCT]>[/][C_TEXT] View API keys [C_PUNCT]>[/][C_TEXT] create an API key and paste it here
'''.strip())


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
    texts = list(map(lambda c: c['text'].strip(), response['choices']))
    if len(texts) == 1:
        richprint(texts[0])
    else:
        terminal_width = shutil.get_terminal_size().columns
        hl_dotted = f"[bright_black]{'·' * terminal_width}[/]"
        richprint(hl_dotted)
        richprint(hl_dotted.join(texts))
        richprint(hl_dotted)

def store_api_key(file_name):
    richprint(api_key_not_found_text)
    api_key = input('> ')
    assert len(api_key) > 0, "an API key will be needed for the app to work"
    lib.write_txt_file_content(file_name, api_key)

def get_openai_api_key():
    file_name = config('OPENAI_API_KEY_FILE_NAME')
    if not os.path.exists(file_name):
        store_api_key(file_name)
    return lib.get_txt_file_content(file_name)

def get_active_profile():
    profiles = config('PROFILES')
    return profiles[0]

def build_completion_params(aiprompt, profile):
    return {
        'model': profile['model'],
        'prompt': f"{profile['prefix']}: {aiprompt}",
        'temperature': profile['temperature'],
        'max_tokens': profile['max_tokens'],
    }

def make_openai_api_request(aiprompt):
    assert len(aiprompt) > 0, "give a prompt to the transformer"
    openai.api_key = get_openai_api_key()
    profile = get_active_profile()
    completion_params = build_completion_params(aiprompt, profile)
    try:
        response = openai.Completion.create(**completion_params)
    except Exception as e:
        raise AssertionError(str(e))
    print_response(response)
