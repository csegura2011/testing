#!/usr/bin/python
#  *-* coding: utf-8 *-*
# quickWeather.py

# References
# - Al Sweigart; 'Automate the Boring Stuff with Python'
#   page 329

import json
import requests


"""
Cryptonator
https://www.cryptonator.com/api
    - Simple Ticker endpoint: https://api.cryptonator.com/api/ticker/btc-usd
    - Complete Ticker endpoint: https://api.cryptonator.com/api/full/btc-usd
    - List of supported currencies: http://www.cryptonator.com/api/currencies
"""

# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.cryptonator.com/api/ticker/btc-usd'
response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)                        # Load JSON data into a Python variable.

# Print ticker data
print '------------------------'
print 'Cryptonator BTC rates'
print '------------------------'
print 'ticker: ', data['ticker']
print 'ticker-base:', data['ticker']['base']            # Base - Base currency code
print 'ticker-target:', data['ticker']['target']        # Target - Target currency code
print 'ticker-price:', data['ticker']['price']          # Price - Volume-weighted price
print 'ticker-volume:', data['ticker']['volume']        # Volume - Total trade volume for the last 24 hours
print 'ticker-change:', data['ticker']['change']        # Change - Past hour price change
print 'timestamp:', data['timestamp']                   # Timestamp - Update time in Unix timestamp format
print 'success:', data['success']                       # Success - True or false
print 'error:', data['error']                       # Success - True or false

"""
- JSON Response
{
    "ticker":{
        "base":"BTC",
        "target":"USD",
        "price":"443.7807865468",
        "volume":"31720.1493969300",
        "change":"0.3766203596"
    },
    "timestamp":1399490941,
    "success":true,
    "error":""
}

Timestamp - Update time in Unix timestamp format

Error - Error description

"""


# Indicadores del día
url = 'http://indicadoresdeldia.cl/webservice/indicadores.json'
response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)

print '--------------------------'
print 'Indicadores del Día Rates '
print '--------------------------'
print 'indicador-ipc:', data['indicador']['ipc']
print 'indicador-uf:', data['indicador']['uf']
print 'indicador-imacec:', data['indicador']['imacec']
print 'indicador-utm:', data['indicador']['utm']
print 'moneda-dolar:', data['moneda']['dolar']
print 'moneda-euro:', data['moneda']['euro']
print 'date:', data['date']

"""
{
    u'restriccion': {
        u'catalitico': [u'no aplica'],
        u'normal_maniana': [u'no aplica'],
        u'normal': [u'no aplica']
    },
    u'santoral': {
        u'maniana': u'Gladys ',
        u'hoy': u'Octavio',
        u'ayer': u'Ruperto'
    },
    u'autor': u'Restart.cl Lab',
    u'indicador': {
        u'ipc': u'0.2',
        u'uf': u'$26.466,82',
        u'imacec': u'1,4',
        u'utm': u'$46.368,00'
    },
    u'version': 2.6,
    u'moneda': {
        u'dolar': u'$663,74',
        u'euro': u'$721,53'
    },
    u'date': u'2017-03-28 17:30:02'

}
"""








