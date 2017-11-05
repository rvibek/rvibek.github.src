Title: Kathmandu daily weather record 1970-2000
Slug: kathmandu-daily-weather-record-1970-2000
Date: 2015-05-13 10:08:43
Modified: 2015-05-13 10:09:43
Tags: dataviz, data, kathmandu, COP20, climatechange, climate change, scraping, WorldClim, NCDC
Category: Blog 
Author: Vibek Raj Maurya 
Lang: EN
Summary: As I watch BBC news report on [COP20](http://www.cop20.pe" target="_blank"), I started searching for the historical climate data in Nepal. I found a couple of sites from where the climate data could be extracted including WorldClim

As I watch BBC news report on [COP20](http://www.cop20.pe" target="_blank"), I started searching for the historical climate data in Nepal. I found a couple of sites from where the climate data could be extracted including WorldClim, but for quick data extraction  [National Climatic Data Center (NCDC)](http://www.ncdc.noaa.gov/" target="_blank") came handy. NCDC has record just for Kathmandu, unfortunately no other places in Nepal.

Downloaded the data and bit of [Google Refine](https://code.google.com/p/google-refine/) and ready to display.


**Kathmandu Daily Weather Record 1970 - 2000 CSV**
[Download RAW CSV](https://docs.google.com/spreadsheets/d/10ZFgeoVtj2JAFkHHwgDhvKYM-ozOHyhsX0j51v4KRRE/export?gid=455851956&format=csv) 

```python
STATION	STATION_NAME	DATE	DateDT	TMAX	TMIN
GHCND:NP000444540	KATHMANDU AIRPORT NP	19980101	01/01/1998	174	13
GHCND:NP000444540	KATHMANDU AIRPORT NP	19980102	02/01/1998	185	35
GHCND:NP000444540	KATHMANDU AIRPORT NP	19980103	03/01/1998	190	6
```
According to available data (from January 1971 to December 2000), **36.6 was recorded in May 7, 1989** and **-3.5 was recorded on January 11, 1978** which are the highest and lowest in the range respectively.

The first graph displays daily maximum and minimum. The second one displays the daily average.

The first graph displays daily maximum and minimum. The second one displays the daily average.
<iframe src="https://docs.google.com/spreadsheets/d/10ZFgeoVtj2JAFkHHwgDhvKYM-ozOHyhsX0j51v4KRRE/pubhtml?gid=570168784&amp;single=true&amp;widget=true&amp;headers=false" width="610" height="450"></iframe>

<iframe src="https://docs.google.com/spreadsheets/d/10ZFgeoVtj2JAFkHHwgDhvKYM-ozOHyhsX0j51v4KRRE/pubhtml?gid=1575144317&amp;single=true&amp;widget=true&amp;headers=false" width="610" height="450"></iframe>