from config import config
from rich import print
import util


def on_no_command(quickparse):
    if quickparse.args:
        util.make_openai_api_request(' '.join(quickparse.parameters))
    else:
        show_help()

def show_help():
    print(util.help_text)
