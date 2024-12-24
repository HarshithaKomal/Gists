import pandas as pd
import plotly.graph_objects as go
from pycoingecko import CoinGeckoAPI
#from mplfinance.original_flavor import candlestick_ohlc
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)
""""days is how many days back from today we want the data"""
"""Checking the type of response data"""
"""Json Expected"""
print(type(bitcoin_data))
bitcoin_price_date = bitcoin_data['prices']
data = pd.DataFrame(bitcoin_price_date,columns=['TimeStamp','Price'])
"""convert the timestamp to datetime and save it as a column called "Date"."""
data['Date']=pd.to_datetime(data['TimeStamp'],unit='ms')
print(data['Date'])
'''Using this modified dataset we can now group by the Date and find the min, max, 
open, and close for the candlesticks'''
candlestick_data = data.groupby(data.Date.dt.date, as_index=False).agg({"Price": ['min','max','first','last']})
'''Plotting the candle stick chart'''
fig = go.Figure(data=[go.Candlestick(x=data["Date"],open=candlestick_data['Price']['first'],high=candlestick_data['Price']['max'],low=candlestick_data['Price']['min'],close=candlestick_data['Price']['last'])])
fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()


