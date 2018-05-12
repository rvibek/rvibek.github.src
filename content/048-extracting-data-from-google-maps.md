Title: Extracting Data from Google Maps
Slug: extracting-data-from-google-maps
Date: 2018-02-12 08:25:16
Modified: 2018-02-12 09:00:00
Tags: google maps, python, scrapping
Category: Blog
Author: Vibek Raj Maurya
Lang: 
Summary: Using the parameter page_token to recursively fetch Google Maps API result.

Google Maps API displays 20 results in one page. By using a parameter ```page_token```, it is possible to get more than 20 results.  The API fetches maximum 60 results for a query. The query can be refined should we need more result - run the query on sub-division level instead of country.

The following code loads the first 20 results, if the JSON file has ```"next_page_token"``` key then it recursively loads the subsequent pages.

The scripts available in my [GitRepo](https://github.com/rvibek/Data-from-Google-Maps)

And here's are the saved results in Gist. [Nepalese Restaurants in Europe](https://gist.github.com/rvibek/e5aea8a9396ad10d5b8d42562c53cf08). Interestingly, there are almost 80 Nepalese restaurants in Finland. 

The script uses 3 libraries. ```time``` is needed to delay the API call. Google has limitation on request per second. 

```
import json
import requests
import time
```

The next is declare the varible and load first JSON
```
# Declare API Key & Query
key = 'AIzaSyXXX-XXXX'
query = 'Nepalese+Restaurants+Finland'
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + str(query) + '&key=' + str(key)

# Parse JSON
jsonfile = requests.get(url)
f = jsonfile.json()
```

The below function recursively populates the result.

```
# Recursive Function
def getjson(url, pagetoken, key, query):

    time.sleep(3)  # API has requests per second limitation

    if pagetoken == '':
        print('url', url)
        pass

    else:

        print('e1url', url)

        # Reset URL
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + str(query) + '&key=' + str(key)
        url = url + '&pagetoken=' + pagetoken

        jsonfile = requests.get(url)
        f = jsonfile.json()

        # append array with desired data from JSON
        for count, name in enumerate(f['results']):
            names.append((f['results'][count]['name']))
            address.append(f['results'][count]['formatted_address'])

        # print(f) #DEBUG
        # Assign NEW Page Token
        try:
            pagetoken = f['next_page_token']
        except KeyError:
            pagetoken = ''
        pass

        # Recursive call
        getjson(url, pagetoken, key, query)
```

