import os
from rich import print as richprint
from rich.console import Console
import openai

import lib
from config import config


console = Console()
prompt = None
profile_index = 1

help_text = lib.apply_color_tags_in_text(lib.get_txt_file_content(config('HELP_FILE_NAME')))

api_key_not_found_text = lib.apply_color_tags_in_text('''
[C_HEAD]OpanAI API key not found[/]
[C_TEXT]Go to [C_LINK]https://beta.openai.com/[/] [C_PUNCT]>[/] [C_TEXT]create an account[/] [C_PUNCT]>[/] [C_TEXT]Profile menu[/] [C_PUNCT]>[/] [C_TEXT]View API keys[/] [C_PUNCT]>[/] [C_TEXT]create an API key and paste it here[/]
'''.strip())


def rich_pformat(rich_string, highlight = False):
    with console.capture() as capture:
        console.print(rich_string, highlight=highlight)
    return capture.get()[:-1]

def get_prompt():
    return rich_pformat(f"{prompt or '[sky_blue3]⟩[/]'} ")

def set_prompt(prompt_str):
    global prompt
    prompt = prompt_str

def update_profile_index(_profile_index):
    global profile_index
    profile_index = _profile_index

def print_profile(index_and_profile):
    index, profile = index_and_profile
    richprint(f"{'[dark_orange]*[/]' if index == profile_index - 1 else ''}[dark_sea_green1]{index+1}[/]: [light_green]{profile['name']}[/]")
    for key, value in profile.items():
        if key != 'name':
            richprint(f"  [hot_pink3]{key}[/][grey53]:[/] [sky_blue2]{value}[/]")

def print_profiles():
    tuple(map(print_profile, enumerate(config('PROFILES'))))

def print_response(response):
    texts = list(map(lambda c: c['text'].strip(), response['choices']))
    if len(texts) == 1:
        richprint(texts[0])
    else:
        richprint(lib.hl())
        richprint(lib.hl().join(texts))
        richprint(lib.hl())

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

def get_active_profile(_profile_index):
    global profile_index
    profiles = config('PROFILES')
    pi = _profile_index or profile_index
    assert 0 <= pi - 1 < len(profiles), f"Index {_profile_index} is out of range, {len(profiles)} profiles are available, use one as 1 <= index <= {len(profiles)}"
    profile_index = pi
    return profiles[profile_index - 1]

def build_completion_params(aiprompt, profile):
    return {
        'model': profile['model'],
        'prompt': f"{profile['prefix']}: {aiprompt}" if len(profile['prefix']) > 0 else aiprompt,
        'temperature': profile['temperature'],
        'max_tokens': profile['max_tokens'],
    }

def print_request_header(profile, completion_params):
    richprint(lib.hl())
    richprint(f"[dark_sea_green1]{profile['name']}[/]")
    richprint(f"[gold3]{completion_params['prompt']}[/]")
    richprint(lib.hl())

def make_openai_api_request(aiprompt, _profile_index):
    assert len(aiprompt) > 0, "give a prompt to the transformer"
    openai.api_key = get_openai_api_key()
    profile = get_active_profile(_profile_index)
    completion_params = build_completion_params(aiprompt, profile)
    print_request_header(profile, completion_params)
    try:
        response = openai.Completion.create(**completion_params)
    except Exception as e:
        raise AssertionError(str(e))
    print_response(response)
    richprint(lib.hl())
