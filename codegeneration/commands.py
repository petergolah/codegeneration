from rich import print as richprint
import util


def on_no_command(quickparse):
    if quickparse.args:
        util.make_openai_api_request(' '.join(map(str, quickparse.parameters)))
    else:
        show_help()

def show_help():
    richprint(util.help_text)
