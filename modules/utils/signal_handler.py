import signal
from colorama import Fore, Style, Back
import sys


def signal_handler(signum, frame):
    if signum == signal.SIGINT:
        print("\n\n\n" + Back.BLACK + Style.BRIGHT + Fore.BLUE + "^C was pressed, exiting...")
        sys.exit()

def set_signal_handler():
    sys.tracebacklimit = -1
    signal.signal(signal.SIGINT, signal_handler)