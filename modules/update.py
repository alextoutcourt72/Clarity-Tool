from os import system as cmd
from utils.exec_script import exec_script

def update():
    cmd("git pull")
    exec_script("main.py")