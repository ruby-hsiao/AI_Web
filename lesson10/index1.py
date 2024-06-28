import requests

youbike_url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?size=2000"

try:
    response = requests.get(youbike_url)
except Exception as e:
    print(e)
else:
    print(response.text)