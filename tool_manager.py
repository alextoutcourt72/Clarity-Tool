# coding=utf-8
import os
import sys
from time import sleep

from core import ClarityTool, ClarityToolsCollection


class UninstallTool(ClarityTool):
    TITLE = "Uninstall Clarity-Tool"
    DESCRIPTION = "Uninstall Clarity-Tool"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable=False, runnable=False)

    def uninstall(self):
        print("Clarity-Tool started to uninstall..\n")
        sleep(1)
        os.system("rd /s /q C:\\Clarity-Tool")
        print("\nClarity-Tool successfully uninstalled... Goodbye.")
        sys.exit()


class ToolManager(ClarityToolsCollection):
    TITLE = "Uninstall | Clarity-Tool"
    TOOLS = [
        UninstallTool()
    ]

if __name__ == "__main__":
    ToolManager().show_options()
