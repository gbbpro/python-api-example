import requests

baseurl = "http://127.0.0.1:5000/process_text"

params = {"text": "hello world py", "duplication_factor": 30, "capitalization": "UPPER"}

resp = requests.get(url=baseurl, params=params)

print(resp.json())
