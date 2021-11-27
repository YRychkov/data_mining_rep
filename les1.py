import requests
from pathlib import Path

temp_file = Path(__file__).parent.joinpath("temp.html")

url = "https://5ka.ru/special_offers/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0"
}

response = requests.get(url, headers=headers)
print(1)
