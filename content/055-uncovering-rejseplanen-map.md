Title: Uncovering Denmark's Transit API
Slug: reverse-engineering-rejseplanen
Date: 2026-01-31 20:51
Modified: 2026-01-31 20:51
Category: Blog
Tags: api, denmark, rejseplanen, python, real-time, transit, ai, llm, kimi
Author: Vibek Raj Maurya
Summary: Reverse engineering [Rejseplanen.dk](https://www.rejseplanen.dk/)'s real-time transit API to understand how trains, metros, and buses move around Copenhagen. Discovered three key APIs, mapped transport codes, and built a system to track route progress using AI-assisted "vibe coding" with the [kimi](https://www.kimi.com/ai-models/kimi-k2-5) k2.5 model.

I have always been fascinated by the real-time visualisations on [rejseplanen.dk](https://www.rejseplanen.dk/). It is really cool to watch trains, metros and buses move around Copenhagen in realtime.

I wanted to delve in and see what is going on behind this app - and understand how the live map in [rejseplanen.dk](https://www.rejseplanen.dk/) worked.

The project also served as a perfect opportunity to experiment with what the community calls "vibe coding" - using AI (specifically the [kimi k2.5](https://www.kimi.com/ai-models/kimi-k2-5) model in [Opencode](https://opencode.ai/). The goal was not just to build a tracker, but to understand the architecture of a complex, real-time transit system.

## The Discovery

I started simple. I first tested with just one API endpoint. I captured
the network traffic from [rejseplanen.dk](https://www.rejseplanen.dk/) live map and began dissecting the query
parameters.

The breakthrough came when I realized the API returns nested arrays, not flat
JSON. A vehicle entry looks like this:

    [" B", 12458213, 55664685, "84/49616/18/19/86", "31", 16, "1", "Buddinge
    St.", [...], ...]

Each index has meaning:
- Index 0: Line identifier
- Index 1-2: X/Y coordinates in a projected coordinate system
- Index 3: Unique vehicle ID
- Index 5: Transport category code
- Index 7: Final destination

## Deciphering the Transport Codes

The real detective work began with the cats parameter. Through a combination of analyzing the web app HTML source code, cross-referencing with live API data, and systematic testing of different category codes, I mapped out the entire transport ecosystem.

Some key discoveries:
- 016 = S-train
- 034 = Metro alternative code
- 070 = Letbane alternative code
- 128 = Havnebus/Waterbus
- 032 = City Bus

## Three API Architecture

The limitation became clear: while the vehicle API tells you where something is, it does not tell you the context. Is the train between stations? Which stations are coming up? How far along the route is it?

So it was time for more digging

**Vehicle API**: Real-time positions, delays, and basic future stops. Returns nested arrays with vehicle coordinates.

**Station API**: All station coordinates and names within a bounding box. Provides the mapping from abstract coordinates to human-readable station names.

**Route Geometry API**: The game-changer. By querying with a specific train_id, this returns the complete route path as ~300 coordinate points, plus station indices showing where each station sits on that path.

<img src="https://res.cloudinary.com/rvibek-com-np/image/upload/v1769889482/reverse_rejseplanen_q8p2zq.png" height="500" />

And, the next steps
1. Fetch all stations in Copenhagen area and build coordinate-to-name lookup
2. Fetch all vehicles to get real-time positions and IDs
3. For each vehicle, fetch its complete route geometry
4. Calculate progress by finding nearest coordinate on route path to current position
5. Determine station context by comparing route index against station indices

The result shows route progress percentage and station status:

    ROUTE PROGRESS: 17.1%
    Position index: 51/298

    STATIONS ON ROUTE:
       PASSED     Rødovre St.
       PASSED     Hvidovre St.
       CURRENT    Danshøj St.
       UPCOMING   Valby St.
       UPCOMING   Carlsberg St.

The complete source code is available on GitHub: [github.com/rvibek/rejseplanen-tracker](https://github.com/rvibek/rejseplanen-tracker)

This project started as simple curiosity about how [rejseplanen.dk](https://www.rejseplanen.dk/) works and evolved into comprehensive reverse engineering of a sophisticated real-time transit API.
