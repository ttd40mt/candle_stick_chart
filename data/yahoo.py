import yfinance as yf

slack = yf.Ticker("MSFT")

history = slack.history(period="max")
print(type(history))

with open("yahoo.csv", mode="w") as df:
    df.write(history.to_csv())
# print(history.to_csv())