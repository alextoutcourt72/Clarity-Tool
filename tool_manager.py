# coding=utf-8
import os
import sys
from time import sleep

from core import ClarityTool, ClarityToolsCollection

class UpdateTool(ClarityTool):
    TITLE = "Update Clarity-Tool"
    DESCRIPTION = "Update Clarity-Tool"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ('Update', self.update)
        ], installable=False, runnable=False)

    def update(self):
        print("Clarity-Tool started to update..\n")
        sleep(1)
        os.system("rd /s /q clarity-tool")
        os.system("git clone https://github.com/alextoutcourt72/clarity-tool.git")
        print("\nClarity-Tool successfully updated... Goodbye.")
        sys.exit()

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
    TITLE = "Uninstall or Update | Clarity-Tool"
    TOOLS = [
        UninstallTool(),
        UpdateTool()
    ]

if __name__ == "__main__":
    ToolManager().show_options()
