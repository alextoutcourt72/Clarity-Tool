# coding=utf-8
import os
import sys
from time import sleep

from core import ClarityTool, ClarityToolsCollection


class UpdateTool(ClarityTool):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update Clarity-Tool", self.update_ht)
        ], installable=False, runnable=False)

    def update_sys(self):
        print("Updating system packages...")
        os.system("powershell -Command \"Set-ExecutionPolicy Bypass -Scope Process -Force; "
                  "iex (New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')\"")
        os.system("choco upgrade all -y")
        os.system("choco install tor openssl curl python3 -y")

    def update_ht(self):
            print("Updating Clarity-Tool...")
            os.system("rd /s /q C:\\Clarity-Tool")
            os.system("mkdir C:\\Clarity-Tool")
            os.system("cd C:\\Clarity-Tool && git clone https://github.com/Al3xUI/Clarity-Tool.git")
            os.system("cd C:\\Clarity-Tool\\Clarity-Tool && powershell ./install.ps1")


class UninstallTool(ClarityTool):
    TITLE = "Uninstall HackingTool"
    DESCRIPTION = "Uninstall HackingTool"

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
    TITLE = "Update or Uninstall | Clarity-Tool"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]

if __name__ == "__main__":
    ToolManager().show_options()
