import plotly.graph_objects as go
import pandas as pd
# read data from gold.csv file and convert do dataframe
df = pd.read_csv("data/gold.csv")

# Config candle stick
candle_stick = go.Candlestick(x=df.time, open=df.open, high=df.high, low=df.low, close=df.close,)

# Draw chart
chart = go.Figure(data=[candle_stick])
# chart.show()
# figure date for xaxis
chart.layout.xaxis.type = "category"
chart.write_html("xauusd.html")
