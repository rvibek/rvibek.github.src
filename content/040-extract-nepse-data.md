Title: POST Method to extract NEPSE Index
Slug: extract-nepse-data
Date: 2015-06-03 13:08:43
Modified: 2017-10-04 16:09:40
Tags: python, scraping, data, NEPSE, pattern, clips, stock
Category: Blog 
Author: Vibek Raj Maurya 
Summary: The script uses `POST` method to pass the variable `topTenBased` from the `select` object and then same page loads the data accordingly.

Fiddling with Nepal Stock Exchange site again. The following script extacts data from [Datewise Idices](http://www.nepalstock.com/datanepse/Indices.php" target="_blank) depending upon the value passed - NEPSE, Sensitive, Float, Banking, Hotels indices are extracted.

The script uses `POST` method to pass the variable `topTenBased` from the `select` object and then same page loads the data accordingly. I hadn't pulled the data from page using `POST` before. 

Here is the source code and the value of different options in *Indices.php*

```
    <select name="topTenBased">  
	  <option value="58">NEPSE</option>
	  <option value="57">Sensitive</option>
	  <option value="62">Float</option>
	  <option value="63">Sen. Float</option>
      .
      .
      .
  </select>
```
The script uses `requests.post` to pass the value 

```python
import requests
from pattern import web

postdata= {
    'topTenBased' : '58', #value from Select menu (NEPSE)
    'Submit' : 'Submit'
    }
r = requests.post('http://www.nepalstock.com/datanepse/Indices.php', data=postdata)
dom = web.Element(r.text)

#Working with local file
# r = open('Indices.htm')
#dom = web.Element(r.read())

#creating DOM and getting the Title corresponding to topTenBased value
data = dom.by_tag('table.dataTable')[1]
title = data.by_tag('td')[0].content
title = title.partition(' ')[0] #title of the table


#Iteration and storing data in array 
def content (idx):
    mydata = []
    for i in range(0, idx):
        ad=d.by_tag('td')[i].content
        mydata.append(ad)
    mydata.append(title)
    print mydata


for d in data.by_class('row1'):
    idx = len(d.by_tag('td'))
    content(idx)
```

**Result**

```javascript
[u'1', u'2014-12-07', u'850.88', u'-2.88', u'-0.34 %', u'462228 ', u'159763214.00 ', u'NEPSE']
[u'2', u'2014-12-08', u'848.41', u'-2.47', u'-0.29 %', u'503962 ', u'158315512.00 ', u'NEPSE']
[u'3', u'2014-12-09', u'848.73', u'0.32', u'0.04 %', u'280049 ', u'159994901.00 ', u'NEPSE']
.
.
.
[u'99', u'2015-05-28', u'841.96', u'4.13', u'0.49 %', u'419834 ', u'179691182.00 ', u'NEPSE']
[u'100', u'2015-05-31', u'871.94', u'29.98', u'3.56 %', u'449995 ', u'200686092.00 ', u'NEPSE']
[u'101', u'2015-06-01', u'890.43', u'18.49', u'2.12 %', u'691694 ', u'273076640.13 ', u'NEPSE']
[u'102', u'2015-06-02', u'901.98', u'11.55', u'1.3 %', u'549899 ', u'246351521.44 ', u'NEPSE']
```
 

**Alternative method**

```python
#Manual extraction - NEPSE Index- passing topTenBased = 58 
for d in data.by_class('row1'):
    date = d.by_tag('td')[1].content
    index = d.by_tag('td')[2].content
    absolute_change = d.by_tag('td')[3].content
    percentage_change = d.by_tag('td')[4].content
    traded_qnt = d.by_tag('td')[5].content
    tranded_amt = d.by_tag('td')[6].content
```

[IPython Notebook](https://wakari.io/sharing/bundle/rvibek/NEPSE_extract_INDEX" target="_blank) in [Wakari](http://www.wakari.io" target="_blank)

Here's my earlier attempt to reproduce the [NEPSE Daily Share Price](http://www.rvibek.com.np/nepse-price-table-reproduced-page/)

