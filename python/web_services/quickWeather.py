#!/usr/bin/python
# quickWeather.py

# References
# - Al Sweigart; 'Automate the Boring Stuff with Python'
#   page 329

import json
import requests
import sys


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print 'Usage: quickWeather.py location'
    sys.exit()
location = '  '.join(sys.argv[1:])


# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % location

response = request.get(url)
response.raise_for_status()


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print wether descriptions.
w = weatherData['list']
print 'Current weather in %s:' % (location)







