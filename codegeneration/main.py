import sys
from quickparse import QuickParse
from reploncli import reploncli
from rich import print as richprint

from util import get_prompt
import commands


commands_config = {
    '': commands.on_no_command,
    ('h', 'help'): commands.show_help,
}

options_config = [
    # ('-a', '--all', bool),
]

def cli_function(cli_args=None):
    try:
        QuickParse(commands_config, options_config, cli_args=cli_args).execute()
    except AssertionError as ae:
        richprint(f"[yellow]{ae}[/]")


if __name__ == '__main__':
    reploncli(cli_function, (sys.argv[1:2] or [''])[0] in ('r', 'repl'), commands.show_help, get_prompt)
