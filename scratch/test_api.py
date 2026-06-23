import json
import urllib.request
import urllib.parse

title = "File:Liverpool logo.svg"
url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"

headers = {'User-Agent': 'MyPortfolioApp/1.0 (contact@myportfolio.com)'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode('utf-8'))
    print(json.dumps(data, indent=2))
