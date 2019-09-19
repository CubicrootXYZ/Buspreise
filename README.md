# Buspreise
Buspreise is a python library to check the prices from long-distance bus in germany and parts of the eu. 

## Installation
1. Download the `includes/buspreise.py`
2. Import it into your project (for example put it in a includes folder like i did and import via `from includes import buspreise`
3. Thats it, have fun

## Functions
Your input is always a start and end (start, destination) city and a date (only the day will be used, no time, please provide a datetime object). 

`getLowestPrice` returns the cheapest connection for the given day. 
`getHighestPrice` returns the most expensive connection for the given day.

Return Object is a Dict with
`['price']` price in Euro as a float
`['duration']` duration of the connection in format `Xh Ymin`
`['departure']` time of departure in format `HH:MM` (24hrs)
`['provider']` simple string with the name from the provider

## Ressources used

This library just scrapes fernbusse.de and parses the site. So be aware, do not make illegal stuff, do not spam the site with requests.
