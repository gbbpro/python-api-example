import requests

baseurl = "https://api-example-mbd8.onrender.com/process_text"

params = {
    "text": "Chicken Fucker lol LOLLOL",
    "duplication_factor": 3000,
    "capitalization": "UPPER",
}

resp = requests.get(url=baseurl, params=params)

print(resp.json())
