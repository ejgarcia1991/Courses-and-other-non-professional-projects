# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:20:20 2020

@author: Eilder Jorge
"""

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_768124.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum=0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    sum+=int(tag.contents[0])
    
print(sum)