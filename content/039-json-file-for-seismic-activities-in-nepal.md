Title: JSON file for seismic activities in Nepal
Slug: json-file-for-seismic-activities-in-nepal
Date: 2015-05-18 13:08:43
Modified: 2015-05-18 14:08:43
Tags: python, scraping, data, earthquake, json, magazine
Category: Blog 
Author: Vibek Raj Maurya 
Lang: EN
Summary: I wrote a python script to reorganise the table containing seismological record from seismonepal.gov.np

Spent the long weekend fiddling with [R](http://cran.r-project.org/" target"=_blank") and [Python](http://python.org" target"=_blank) mainly to pull the data - and then cleaning and reorganising.

Among others, I wrote a python script to reorganise the table containing seismological record from [seismonepal.gov.np](http://seismonepal.gov.np" target="_blank") website.

**=ImportHTML()** is a handy function to fetch the data from a table or list. It time saver trick in [Google Spreadsheet](http://spreadsheet.google.com" target="_blank") when the source data is available in a tabular or list form. 

```python
=ImportHTML("http://seismonepal.gov.np/index.php", "table", 1)
``` 

Next, a python script converts data in English into Nepal

```python
#List of character/word to be replaced
replaceDict = {
	'1':'१'	,
	'2':'२'	,
	'3':'३'	,
	'Local Time' : 'LocalTime',
	'Magnitude(ML)' : 'Magnitude',
	'Achham' : 'अछाम'	,
	'Arghakhanchi' : 'अर्घाखाँची'	,
	'Baglung' : 'बाग्लुङ'	
    }
    
 #Function to replace word 
 def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
    
 #Iteration
 with open('earthquake.csv', 'rb') as csvfile:
	earthquake = csv.reader(csvfile, delimiter=',')

	for row in range(record2read):
		
		row = [word.replace('*','') for word in earthquake.next()]
		row = ' '.join(row).encode('utf-8')
		row = replace_all(row, replaceDict)
		
```

And writing the result into [JSON](http://app-weather.rhcloud.com/data/earthquake/earthquake.json" target="_blank") format with Nepali data. 


```javascript
{
    "earthquake": [
        {
            "MM": "५",
            "DD": "१७",
            "Longitude": "८५.८७",
            "Epicentre": "रामेछाप",
            "Magnitude": "४.६",
            "YYYY": "२०१५",
            "Remarks": "NSC",
            "Date": "१७/०५/२०१५",
            "Latitude": "२७.४८",
            "LocalTime": "११:३०"
        },
        {
            "MM": "५",
            "DD": "१७",
            "Longitude": "८६.०६",
            "Epicentre": "दोलखा",
            "Magnitude": "४.४",
            "YYYY": "२०१५",
            "Remarks": "NSC",
            "Date": "१७/०५/२०१५",
            "Latitude": "२७.७३",
            "LocalTime": "०५:००"
        },
        {
            "MM": "५",
            "DD": "१६",
            "Longitude": "८६.१४",
            "Epicentre": "दोलखा",
            "Magnitude": "४.३",
            "YYYY": "२०१५",
            "Remarks": "NSC",
            "Date": "१६/०५/२०१५",
            "Latitude": "२७.६४",
            "LocalTime": "२०:४४"
        }]}
```
Finally - widget based on above JSON file. [HimalKhabar](http://himalkhabar.com" target="_blank") has embedded it in its website.

![Seismic Activity Card](https://res.cloudinary.com/rvibek-com-np/image/upload/w_350,e_shadow/v1628804084/reu56ezdegh7pkymfg9w.png)


<blockquote class="twitter-tweet" lang="en"><p lang="ne" dir="ltr">भूकम्पको लाइभ अपडेट <a href="http://t.co/yfbJgjRYxA">http://t.co/yfbJgjRYxA</a> मा ।</p>&mdash; Himal Khabar (@Himal_Khabar) <a href="https://twitter.com/Himal_Khabar/status/600229390790721538">May 18, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>