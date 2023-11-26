import requests

TOKEN = "pk_6d56d3ebdd9e4f60bd737c118e5904cf"
SYMBOL = "AAPL"

# URL = f"https://api.iex.cloud/v1/data/core/historical_prices/{SYMBOL}"
URL = 'https://api.iex.cloud/v1/data/core/historical_prices/{}?token={}'.format(SYMBOL, TOKEN)
param = {
    # "symbol": SYMBOL,
    "range": "2m",
    # "token": TOKEN
}

data = requests.get(URL, params=param)
# clear_data = data.content[2:]

print(data.reason)
for item in data.content:
    print(item)
print(type(data.content))
print(data.content)
print(len(data.content))