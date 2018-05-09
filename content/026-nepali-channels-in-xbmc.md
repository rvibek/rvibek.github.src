Title: Nepali TV Channels in XBMC
Slug: nepali-channels-in-xbmc
Date: 2012-10-12 10:05:43
Modified: 2012-10-12 10:06:43
Tags: nepali, nepal, xbmc, addon, ntv, sagarmatha, navix, navi-x
Category: Blog 
Author: Vibek Raj Maurya 
Lang: EN
Summary: For those who are interested in watching Nepali and Indian TV Channels in a TV, I recommend [XBMC](http://xbmc.org/" target="_blank") (available on Windows, Linux, Mac, Android, AppleTV etc) and install [Navi-X](http://code.google.com/p/navi-x/" target="_blank") addon.

I have been outside of Nepal for quite sometime now. For news report and TV program, I logon to [canadanepal.net](http://canadanepal.net" target="_blank") among others to flick through the items. Since I am using raspberry pi as a media center, I thought of porting videos in my telly. 

For those who are interested in watching Nepali and Indian TV Channels in a TV, I recommend [XBMC](http://xbmc.org/" target="_blank") (available on Windows, Linux, Mac, Android, AppleTV etc) and install [Navi-X](http://code.google.com/p/navi-x/" target="_blank") addon. Refer to wiki on Navi-X code page for installation details.

I run [Raspbmc](http://www.raspbmc.com/" target="_blank"), a debian based distro for [Raspberry Pi](http://raspberrypi.org" target="_blank"), connected to Samsung P2370HD and controlled by [XBMC Remote](https://play.google.com/store/apps/details?id=org.xbmc.android.remote&hl=en" target="_blank") – works flawlessly. I am also running XBMC in my Windows and Linux, plus in Google Nexus (I have issues with sound in my phone though).

I have added a few Nepali TV channels (NTV, NTV Plus and Sagarmatha) and some Youtube channels to Navi-X repository. The TV channels stream live. I shall keep updating the repository as I get new feeds.

```
Search “nepal” in Navi-X.

Right click and save the result – “Nepali TV” to your favourite.
```


Happy watching!

![NepaliTV](https://res.cloudinary.com/rvibek-com-np/image/upload/v1423918809/NepaliTV_Navi-X_z7y0t5.png)


*Update: November 2014*
I have put the [JSON of latest playlist](https://app-weather.rhcloud.com/data/kimplx.json" target="_blank") publicly - if you are interested in building up your own app.

Here's  the snapshot of generated JSON. The file gets updated every hour.

```javascript
{
    "videolist":  [
           
            {
                "title": "Cristiano Ronaldo did NOT donate $8 million to the Save the Child",
                "url": "http://www.youtube.com/embed/d_Qt2fdMrn8",
                "rating": "1.00"
            },
            {
                "title": "Nepal earthquake: Devastated town waits for government help",
                "url": "http://www.youtube.com/embed/RDlodjScM_4",
                "rating": "1.00"
            },
            {
                "title": "Plastic Tirpal crisis in Kathmandu",
                "url": "http://www.youtube.com/embed/mLC5fnkORXg",
                "rating": "1.00"
            
        ]
    }
}
```