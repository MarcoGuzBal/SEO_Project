import requests
import os

API_KEY=os.environ.get('EXCHANGERATE_API_KEY')

url=f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

response = requests.get(url)

print(response.json())
