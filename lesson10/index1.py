import requests

youbike_url = ""

try:
    response = requests.get(youbike_url)
except Exception as e:
    print(e)
else:
    print(response.text)