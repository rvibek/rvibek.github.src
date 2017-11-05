Title: CSV from Drishti KTM Valley Air Quality
Slug: csv-from-drishti-kathmandu-valley-air-quality
Date: 2016-08-18 21:25:38
Tags: kathmandu, dataviz, python, bokeh, air quality
Category: Blog
Author: 
Lang: EN
Summary: The sheets provided just a snapshot of past 24 hours data. I wish they had shared more data or perhaps API - reachers and data enthusiasts would have loved it. 

I ran across a couple posts on [Drishti Kathmandu](https://www.facebook.com/groups/drishtiKathmandu/" target="_blank") recently. I was excited to read, as some tweets indicated, Drishti Kathmandu had installed low-cost pollution monitoring stations in various spots in the valley and would be sharing real time air quality monitoring data. 

Drishti Kathmandu maintains a [Google Sheets](https://docs.google.com/spreadsheets/d/1J2I40hglES63YZHROcOL3oAjDPqiiKLRPE_ikAWsR-Q/pubhtml?gid=1267634591&single=true" target="_blank"). The sheet gets updated every hour but the readings doesn't change much though. Besides, I was disappointed the sheets provided just a snapshot of past 24 hours data. I wish they had shared more data or perhaps API - reachers and data enthusiasts would have loved it. I once wrote to group admin but never heard back.

As a weekend project, I wrote a python script to scrap the sheets and append reading to [CSV file](http://goo.gl/y2Z0gG" target="_blank"). 

Primarily, I have used [CLiPs pattern module](http://www.clips.ua.ac.be/pattern" target="_blank") for screen scrapping. Regular expression [re](https://docs.python.org/2/library/re.html" target="_blank") module to clean up HTML.


The [CSV file](http://goo.gl/y2Z0gG" target="_blank") looks as follows
```javascript
date,time,place,reading,type
"Sunday,July 31,2016","08:00 AM","GONGABU",9,R
"Sunday,July 31,2016","11:00 AM","KALANKI",29,R
"Sunday,July 31,2016","10:00 AM","KOTESHWOR",15,R
"Sunday,July 31,2016","06:00 AM","NEW BANESHWOR",37,R
"Sunday,July 31,2016","11:00 AM","PUTALISADAK",19,R
"Sunday,July 31,2016","11:00 AM","KALANKI",18,R
...
...
"Thursday,August 18,2016","10:00 AM","GONGABU",12,H
"Thursday,August 18,2016","10:00 AM","KALANKI",63,H
"Thursday,August 18,2016","09:00 AM","KOTESHWOR",83,H
"Wednesday,August 17,2016","09:00 AM","MAHARAJGUNJ",34,H
"Wednesday,August 17,2016","00:00 PM","PUTALISADAK",29,H
"Wednesday,August 17,2016","07:00 AM","SAATDOBATO",44,H
"Wednesday,August 17,2016","08:00 PM","THAPATHALI",95,H
```

The flag R and H means Hourly reading and the Highest in the past 24 hours. I started appending Highest reading a week ago.

Graph generated from the data collected in about a month

![Graph](http://res.cloudinary.com/rvibek-com-np/image/upload/v1472802171/drishti-aug_ooogyl.png)



**Related tweets**
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Exceptionally good <a href="https://twitter.com/hashtag/air?src=hash">#air</a> today <a href="https://twitter.com/hashtag/airpollution?src=hash">#airpollution</a> <a href="https://twitter.com/hashtag/drishtikathmandu?src=hash">#drishtikathmandu</a> <a href="https://twitter.com/hashtag/kathmandu?src=hash">#kathmandu</a><br>realtime data @ <a href="https://t.co/4TaS5UKf2J">https://t.co/4TaS5UKf2J</a> <a href="https://t.co/kIa6Kc2Uxp">pic.twitter.com/kIa6Kc2Uxp</a></p>&mdash; Vogmask Nepal (@vogmask_nepal) <a href="https://twitter.com/vogmask_nepal/status/749807273350868994">July 4, 2016</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Glad to see KTM&#39;s <a href="https://twitter.com/hashtag/AirQuality?src=hash">#AirQuality</a> data (updated every 5 mins from 9 spots). Hope it&#39;s used for action <a href="https://twitter.com/hashtag/DrishtiKathmandu?src=hash">#DrishtiKathmandu</a> <a href="https://t.co/yNaLxaWli2">https://t.co/yNaLxaWli2</a></p>&mdash; Bhushan Tuladhar (@BhushanTuladhar) <a href="https://twitter.com/BhushanTuladhar/status/749484719981506561">July 3, 2016</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>