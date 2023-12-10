import requests

baseurl = "http://127.0.0.1:5000/uppercase"

params = {"text": "hello world py"}

resp = requests.get(url=baseurl, params=params)

print(resp.json())
