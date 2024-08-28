from core import ClarityTool, ClarityToolsCollection


class SpiderFoot(ClarityTool):
    TITLE = "SpiderFoot"
    DESCRIPTION = "SpiderFoot is an open source intelligence automation tool that enables organizations to perform threat intelligence assessments."
    PROJECT_URL = "https://github.com/smicallef/spiderfoot"

    INSTALL_COMMANDS = [
        "git clone https://github.com/smicallef/spiderfoot.git",
        "cd spiderfoot",
        "pip3 install -r requirements.txt",
        "python3 sf.py"
    ]

class OSINTTools(ClarityToolsCollection):
    TITLE = "OSINT Tools"
    TOOLS = [
        SpiderFoot()
    ]