import sys
from quickparse import QuickParse
from reploncli import reploncli

import commands
from lib import CLR


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
        print(f"{CLR.yellow}{ae}{CLR.reset}")

if __name__ == '__main__':
    reploncli(cli_function, (sys.argv[1:2] or [''])[0] in ('r', 'repl'), commands.show_help, f"{CLR.yellow}»{CLR.reset} ")