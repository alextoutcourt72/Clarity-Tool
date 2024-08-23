import json
import requests
import urllib


# You may need to install Requests pip
# python -m pip install requests

class IPQS:
    key = 'YOUR_API_KEY_HERE'

    def malicious_url_scanner_api(self, url: str, vars: dict = {}) -> dict:
        url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
        x = requests.get(url, params=vars)
        print(x.text)
        return (json.loads(x.text))


if __name__ == "__main__":
    link = input("entrez le lien à scanner [>] ")
    URL = link

    # Adjustable strictness level from 0 to 2. 0 is the least strict and recommended for most use cases. Higher strictness levels can increase false-positives.
    strictness = 0

    # custom feilds
    additional_params = {
        'strictness': strictness
    }

    ipqs = IPQS()
    result = ipqs.malicious_url_scanner_api(URL, additional_params)

    if 'success' in result and result['success'] == True:
        print(result)