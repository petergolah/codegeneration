from config import config

from lib import (
    CLR,
)


help_text = '''
CLR_SEPARATORGeneralCLR_RESET
CLR_COL1codegeneration help  CLR_SEPARATOR-CLR_RESETCLR_COL2  see this helpCLR_RESET
CLR_COL1codegeneration repl  CLR_SEPARATOR-CLR_RESETCLR_COL2  start CodeGeneration in REPL modeCLR_RESET
'''.strip().replace('CLR_COL1', CLR.l_blue).replace('CLR_SEPARATOR', CLR.l_black).replace('CLR_COL2', CLR.blue).replace('CLR_RESET', CLR.reset)
