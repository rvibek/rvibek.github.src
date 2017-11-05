Title: Nepali news video PLX
Slug: nepali-news-video-plx
Date: 2015-05-13 13:08:43
Modified: 2015-05-13 14:08:43
Tags: dataviz, data, kimono, xbmc, plx, navix, nepal, kodi, scraping
Category: Blog 
Author: Vibek Raj Maurya 
Lang: EN
Summary: In 2013, I had created *Nepal TV* channel feed in Navi-X to watch [Nepal Television](http://ntv.org.np" target="_blank"), [BBC Sajha Sawal](https://www.youtube.com/user/bbcsajhasawal" target="_blank") and some more nepali news feeds.  

Here's my python script that populates Nepali news brief videos into [NaviX](https://code.google.com/p/navi-x/" target="_blank") in [XMBC/Kodi](http://kodi.tv" target="_blank"). In 2013, I had created *Nepal TV* channel feed in Navi-X to watch [Nepal Television](http://ntv.org.np" target="_blank"), [BBC Sajha Sawal](https://www.youtube.com/user/bbcsajhasawal" target="_blank") and some more nepali news feeds.  

I have setup [Kimono](https://www.kimonolabs.com/" target="_blank"") to scrap video list from [CanadaNepal](http://www.canadanepal.net" target="_blank"). The following file in [OpenShift](http://www.openshift" target="_blank") is updated every hour 
[kimplx.plx](http://app-weather.rhcloud.com/data/kimplx.plx" target="_blank") which is loaded in Navi-X. Search for *Nepali TV* in Navi-X to see the listings.

**Python Code**
```python
import json
import urllib
import datetime

results = json.load(urllib.urlopen("http://goo.gl/5sUcpr"))

items = results["results"]["videolink"]
myfile = open("/data/kimplx.plx", "w")

x = "version=1\n"
x+= "background=http://goo.gl/rpxPsc\n"
x+= "title=News Playlist\n"
x+= "logo=http://rvibek.com/public/logo.png\n"
x+= "description=Updated"+str(datetime.datetime.utcnow())+"/description\n"

for item in items:
	# x+= "#"
	x+= "type=video\n"
	x+= "name="+item["title"]["text"].encode('utf-8')+"\n"
	x+= "thumb=http://goo.gl/YHRb3u"+"\n"
	if item.has_key('href'):
		x+= "URL="+item["href"].encode('utf-8')+"\n"
	x+= "player=default\n"
	x+= "rating=-1.00\n"
	x+= "\n"

myfile.write(x)
print x
```

**Generated PLX file**
```javascript
...
rating=-1.00

type=video
name=Tribhuvan international airport to be improved
thumb=YouTube-logo-full_color.png
URL=http://www.youtube.com/embed/PSjFlbzpg9Y
player=default
rating=-1.00

type=video
name=Human Trafficking Till When?
...
```


**Result in Navi-X**
![News brief](http://res.cloudinary.com/rvibek-com-np/image/upload/q_63/v1423918809/NepaliTV_Navi-X_z7y0t5.png)


**Add Nepali Channel to your Favlist**
I have added a few Nepali TV channels (NTV, NTV Plus and Sagarmatha) and some Youtube channels to Navi-X repository. The TV channels stream live. I shall keep updating the repository as I get new feeds.

```
Search “nepal” in Navi-X.

Right click and save the result – “Nepali TV” to your favourite.
```

[Refer following page for more about Nepali Channels in XBMC/Kodi](http://rvibek.com/nepali-channels-in-xbmc/" target="_blank")