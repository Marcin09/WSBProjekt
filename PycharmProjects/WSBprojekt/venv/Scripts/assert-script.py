#!C:\Users\marci\PYCHARM\PycharmProjects\WSBprojekt\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'assert==0.1.0','console_scripts','assert'
__requires__ = 'assert==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('assert==0.1.0', 'console_scripts', 'assert')()
    )
