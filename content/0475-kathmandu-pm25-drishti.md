Title: Kathmandu PM2.5 Plot
Slug: kathmandu-pm25-drishti
Date: 2017-11-16 08:25:16
Modified: 2017-11-16 08:25:16
Tags: google matplotlib, python, kathmandu, nepal, drishti, air quality
Category: Blog
Author: Vibek Raj Maurya
Lang: 
Summary: Using page_token parameter to recursively fetch Google Maps API result.

The `plt.xkcd()` function can convert any matplotlib plot into XKCD style. Trying it with [Kathmandu air quality data](https://github.com/rvibek/drishti) collected over a year.

![ktm_air_quality_pm25](http://res.cloudinary.com/rvibek-com-np/image/upload/v1510877205/ktm_air_quality_pm25_gukcmg.png)

### Import Library

```python
import matplotlib

plt.xkcd()
font = {'family': 'xkcd','weight' : 'regular','size'   : 12}
matplotlib.rc('font', **font)
```



### Plot Graph

```python
places = ['SATDOBATO', 'THAPATHALI', 'KALANKI', 'PUTALISADAK']
fig = plt.figure(figsize=(10,10))

for idx in range(len(places)):
    ax = fig.add_subplot(2, 2, idx+1)

    tmp = df[df.place == places[idx]]
    tmp.set_index('date', inplace=True)

    tmpweekly = tmp.resample('W').mean()
    ax.plot(tmpweekly.index, tmpweekly.reading, label='Weekly PM2.5 AVG')
    plt.tight_layout()
    plt.legend()


    tmpmonthly = tmp.resample('M').mean()
    ax.plot(tmpmonthly.index, tmpmonthly.reading, label='Monthly PM2.5 AVG')
    plt.legend()
    plt.title(places[idx]+'  PM2.5 READING', size= 16)

plt.show()
```


Check out [matplotlib xkcd gallery](https://matplotlib.org/xkcd/examples/showcase/xkcd.html) for more.

