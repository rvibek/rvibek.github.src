Title: Basemap and xkcd() in Matplotlib
Slug: basemap-and-xkcd-in-matplotlib
Date: 2017-09-15 21:25:38
Modified: 2017-09-29 20:25:59
Category: Blog
Tags: matplotlib, python, southasia, nepal
Author: Vibek Raj Maurya
Lang: EN
Summary: I had never paid much attention what goes under the hood and barely used customisations. It was time to roll up the sleeves for yet another tutorial. 

It had been awhile since I last posted.

I have been following [santdex's YouTube](https://www.youtube.com/user/sentdex){:target="_blank"} for tutorials. Although I had been using some [matplotlib](https://matplotlib.org){:target="_blank"}, I had never paid much attention what goes under the hood and barely used customisations. It was time to roll up the sleeves for yet another tutorial. 

I have been 'binge' watching [Matplotlib Tutorial Series - Graphing in Python](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF){:target="_blank"}. And, here's one of the works - [xkcd](https://xkcd.com){:target="_blank"} styled map of South Asia. 

[![xkcd South Asia](http://res.cloudinary.com/rvibek-com-np/image/upload/v1505491453/xkcd_southasia_xkcd_ag53g2.png)](http://res.cloudinary.com/rvibek-com-np/image/upload/v1505491453/xkcd_southasia_xkcd_ag53g2.png){:target="_blank"}

[Download SVG](http://res.cloudinary.com/rvibek-com-np/image/upload/v1505491459/xkcd_southasia_xkcd_fbryap.svg){:target="_blank"}



```python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import requests

plt.xkcd()


font = {
		'family': 'xkcd',
		'size'   : 4.5}

matplotlib.rc('font', **font)

#get capital cities' coordinates
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQT6XItC-X5LNOYb2Nh7kPk5ANxHkoFLX8wRXBD0ywD8zNDRCdTKCt0V6bw9A3Y4XLCpgs-NDNUr-Qm/pub?gid=1498534080&single=true&output=csv'
df = pd.read_csv(url)


ax1 = plt.subplot(111)

m = Basemap(projection = 'mill', 
			llcrnrlat=2,llcrnrlon=60,urcrnrlat=40, urcrnrlon=98,
			ax = ax1)
m.drawcountries(linewidth=0.5)
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color="grey")
m.drawmapboundary()


for point in range(len(df)):
	x,y = m(df.Longitude[point], df.Latitude[point])
	ax1.annotate(df.Capital[point], xy=(x,y), xycoords='data',
				textcoords='offset points', xytext=(0,5))
	ax1.plot(x,y, marker='o', color='indianred')

plt.title('xkcd - South Asia', size=16)

#saving file
#plt.savefig('xkcd_southasia.png', format='png', dpi=600)

plt.show()

```

Check out [xkcd showcase in matplotlib site](https://matplotlib.org/xkcd/examples/showcase/xkcd.html"){:target="_blank"} for more
