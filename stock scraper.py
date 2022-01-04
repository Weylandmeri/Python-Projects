import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#https://www.marketwatch.com/investing/cryptocurrency/{TICKER}
#https://www.marketwatch.com/investing/stock/TSLA

TICKER = "TSLA"

def get_stock(TICKER):
	url = f"https://www.marketwatch.com/investing/stock/{TICKER}"
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	price = float(soup.find('h2', {"class":"intraday__price"}).text.replace(",", "")[3:-1])
	return price


fig, ax = plt.subplots(figsize=(6, 3), dpi=100, facecolor="#212946")
ax.set_facecolor("#2A3459")
plt.ticklabel_format(style='plain', useOffset=False, axis='y')
#ax.ticklabel_format(useOffset=False, style='plain')

X = []
Y = []

def animate(x):
	Y.append(get_stock(TICKER))
	X.append(len(Y))
	ax.clear()
	ax.plot(X,Y, color = "#00ff41", label="Price")
	title = ax.set_title(f"${Y[-1]}", fontsize="25")
	plt.setp(title, color="#00ff41") 
	ax.set_xlim([max(X)-50, max(X)])


ani = animation.FuncAnimation(fig, animate, interval = 500)
plt.show()