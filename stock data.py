import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from alpha_vantage.timeseries import TimeSeries
import datetime as dt
import numpy as np

fig, ax = plt.subplots(figsize=(15, 5), dpi=70, facecolor="#212946")

start = dt.datetime.now() - dt.timedelta(days=30)
end = dt.datetime.now()

TICKER = "TSLA"
KEY = "YOUR KEY" # Enter in your alpha vantage API key

#ts = TimeSeries(key=KEY, output_format='pandas')
#data, meta_data = ts.get_intraday(symbol=TICKER,interval='60min', outputsize='full')['4. close'].values

dates = mdates.drange(start, end, dt.timedelta(weeks=3))


data = web.DataReader(TICKER, "av-daily", start, end, api_key=(KEY))
datetime = data.index.values


y = [i for i in range(0,len(datetime))]
ylist = []

for i in data.close:
	ylist.append(i)
xlist = []

for i in range(0, len(ylist)):
	xlist.append(i)

ax.tick_params(colors='white', which='both')
plt.plot_date(datetime, y, visible=False)
plt.gcf().autofmt_xdate(rotation = 90)




plt.figure(1, dpi=120)
plt.grid()
plt.xlabel("Time", color="#F5D300")
plt.ylabel("Price", color = "#F5D300")

# X and Y Axis Modification
ax.axhline(linewidth=1, color=".8")
ax.axvline(linewidth=1, color=".8")

plt.grid(color = "0.5")

plt.plot(xlist, ylist, label=TICKER, color = "#00ff41")
#plt.plot(xlist, log, label="Derivative", color="#F5D300")

# Color Behind Grid
ax.set_facecolor("#2A3459")
# Crop the Viewport
ax.set_xlim([0, max(xlist)])
ax.set_ylim([0-.01*min(ylist), max(ylist)*1.1])
# Equal Aspect Ratio
plt.gca().set_aspect("auto")

plt.legend()
plt.show()