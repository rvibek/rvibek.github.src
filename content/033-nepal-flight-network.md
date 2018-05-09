Title: Nepal Flight Network
Slug: nepal-flight-network
Date: 2014-09-26 10:05:43
Modified: 2014-09-26 10:06:43
Tags: airport, flight, R, dataviz, nepal, domestic airports
Category: Blog 
Author: Vibek Raj Maurya 
Lang: EN
Summary: I had long planned to fly to Nairobi during the weekend but at the very last moment the agent said the flight was ‘full-booked’

It was a lazy weekend here in Hargeisa.  I had long planned to fly to Nairobi during the weekend but at the very last moment the agent said the flight was ‘full-booked’ and they don’t have seats until Monday.

The flight reminds me of [flight dataviz](http://flightclub.jalopnik.com/you-must-see-this-stunning-illustration-of-european-air-1540684842" target="_blank) I saw sometime ago – very stunning work. I am motivated to start aggregating flight schedule data in Nepal, may be someday I am able to create animated visualisation of flight network in Nepal.  
  
As for now I have flight network in the simplest form. I aggregated the flight connection data from [TravelandTourNepal](http://travelandtourtonepal.com/ticketing/domestic-flight-in-nepal" target="_blank) and airport data from [Wikipedia – Airport in Nepal](http://en.wikipedia.org/wiki/List_of_airports_in_Nepal" target="_blank). I loaded the resulting two files in [R](http://www.r-project.org/) and fiddled with [map library](http://cran.r-project.org/web/packages/maps/index.html" target="_blank).

[![FlightNetwork Nepal](https://i0.wp.com/res.cloudinary.com/rvibek-com-np/image/upload/v1423914262/FlightNetwork_ahrp5v.png?resize=605%2C305)](http://i0.wp.com/res.cloudinary.com/rvibek-com-np/image/upload/v1423914262/FlightNetwork_ahrp5v.png "Flight Network")

**flights.csv**
```python
airline,airport1,airport2,cnt 
ALL,KTM,BDP,300 
ALL,KTM,BWA,500
ALL,KTM,BHR,500 
ALL,KTM,BIR,900
```

**airports.csv**
```python
iata,airport,city,state,country,lat,long
KTM,TribhuwanAirport,Kathmandu,BG,Nepal,27.6963889,85.3588889 
PKR,PokharaAiport,Pokhara,GD,Nepal,28.2008333,83.9819444 
BWA,GautamBuddha,Bhairahawa,LM,Nepal,27.5055556,83.4161111
```

**R programme**
```python
library('maps')
library('geosphere')
library('mapdata')

airports <- read.csv("airports.csv", header=TRUE) 
flights <- read.csv("flights.csv", header=TRUE, as.is=TRUE)

xlim<-c(80.3,88.2)
ylim<-c(26,30.3)

pal <- colorRampPalette(c("#f2f2f2", "black"))
colors <- pal(100)

#map("world", regions = "nepal", col="#f2f2f2", fill=T, bg="white", lwd=0.05, xlim=xlim, ylim=ylim)
map('worldHires', 'Nepal', col="#f2f2f2", fill=T)

fsub <- flights[flights$airline == "ALL",]
fsub <- fsub[order(fsub$cnt),]
maxcnt <- max(fsub$cnt)
for (j in 1:length(fsub$airline)) {
  air1 <- airports[airports$iata == fsub[j,]$airport1,]
  air2 <- airports[airports$iata == fsub[j,]$airport2,]
  
  inter <- gcIntermediate(c(air1[1,]$long, air1[1,]$lat), c(air2[1,]$long, air2[1,]$lat), n=100, addStartEnd=TRUE)
  colindex <- round( (fsub[j,]$cnt / maxcnt) * length(colors) )
  
  lines(inter, col=colors[colindex], lwd=0.8)
}
```


