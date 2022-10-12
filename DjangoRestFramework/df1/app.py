import json
import requests

URL = "http://127.0.0.1:8000/stup/"

p = requests.get(url=URL)
data = p.json()

print(data)
