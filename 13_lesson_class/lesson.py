import requests

resource = requests.get("https://www.work.ua")
print(resource.text)