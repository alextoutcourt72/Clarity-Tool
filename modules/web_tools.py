from core import ClarityToolsCollection, ClarityTool


class wpscan(ClarityTool):
    TITLE = "WPScan"
    DESCRIPTION = "WPScan is a free, for non-commercial use, black box WordPress Vulnerability Scanner written for security professionals and blog maintainers to test the security of their WordPress websites. [!] install ruby for use wpscan"

    PROJECT_URL = "https://wpscan.org/"

    INSTALL_COMMANDS = [
        "git clone https://github.com/wpscanteam/wpscan.git",
        "winget install -e --id=Ruby.Ruby",
        "gem install bundler",
        "bundle install",
        "cd wpscan"
        "bundle config set path 'vendor/bundle' && bundle install"
    ]
    RUN_COMMANDS = ["cd wpscan && bundle exec rake wpscan"]

class WebTools(ClarityToolsCollection):
    TITLE = "Web Tools"
    TOOLS = [
        wpscan()
    ]

