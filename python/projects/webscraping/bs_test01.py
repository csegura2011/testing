#!/usr/bin/python
# -*- coding: utf-8 -*-

# File:
# Author: Cristian Segura <cristian.segura.lepe@gmail.com>
# Creation Date: 2017/04/05

from bs4 import BeautifulSoup

import urllib

r = urllib.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
soup = BeautifulSoup(r)
print type(soup)


