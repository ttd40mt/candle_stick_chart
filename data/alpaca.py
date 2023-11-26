import requests, json, csv
from datetime import datetime

API_KEY = "DlFOrYX_BLmWhwEH8d2QzAcZO_2FiwrQ"
SYMBOL = "C:XAUUSD"
URL = "https://api.polygon.io/v2/aggs/ticker"
multiplier = 1
timespan = "day"
time_from = "2021-01-10"
time_to = "2023-11-20"
URL = 'https://api.polygon.io/v2/aggs/ticker/{}/range/{}/{}/{}/{}?apiKey={}'.format(SYMBOL, multiplier, timespan,
                                                                                    time_from, time_to, API_KEY)
# params = {
#     "stocksTicker": SYMBOL,
#     "multipler": "1",
#     "timespan": "day",
#     "from": "2023-11-10",
#     "to": "2023-11-20",
#     # "apiKEY": API_KEY,
# }
# Get Gold data from polygon.io
response = requests.get(URL)
data = response.content

# Convert data type from byte to json
json_viewer = json.loads(data)
print(json_viewer)

csv_file = open("gold.csv", mode="w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['time', 'open', 'high', 'low', 'close'])
print(json_viewer)
for item in json_viewer["results"]:
    formatted_time = datetime.fromtimestamp(item['t']/1000)
    date_only = formatted_time.strftime("%Y-%m-%d")
    print(date_only)
    # print(formatted_time)
    open_price = item["o"]
    high_price = item["h"]
    low_price = item["l"]
    closed_price = item["c"]
    csv_writer.writerow([date_only, open_price, high_price, low_price, closed_price])
csv_file.close()
