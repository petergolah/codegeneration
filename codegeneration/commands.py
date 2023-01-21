from config import config
import util
from lib import (
    CLR,
    cprint,
)


def on_no_command(quickparse):
    if quickparse.args:
        cprint("Unknown: '%s'  //  ask for 'help'" % (' '.join(quickparse.args), ), CLR.yellow)
    else:
        show_help()

def show_help():
    print(util.help_text)
