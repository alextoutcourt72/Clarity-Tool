import os

from core import ClarityTool, ClarityToolsCollection


class holehe(ClarityTool):
    TITLE = "Holehe"
    DESCRIPTION = "A Passive DNS / Domain Name System (DNS) reconnaissance tool"
    PROJECT_URL = "https://github.com/megadose/holehe"

    INSTALL_COMMANDS = [
        "pip3 install holehe",
    ]

    def run(self):
        self.before_run()
        target = input("Give me the target: ")
        os.system(f"cd holehe && python3 holehe.py -d {target}")
        self.after_run()

class OSINTTools(ClarityToolsCollection):
    TITLE = "OSINT Tools"
    TOOLS = [
        holehe()
    ]