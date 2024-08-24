from subprocess import call
import sys
from time import sleep


def exec_script(path):
    try:
        call([sys.executable, path])
    except Exception as e:
        return e
