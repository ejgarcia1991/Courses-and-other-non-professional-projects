# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:38:04 2020

@author: Eilder Jorge
"""



import urllib.request, urllib.parse, urllib.error
import json

url = ('http://py4e-data.dr-chuck.net/comments_768127.json')
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)

sum=0
for item in info['comments']:
    sum+=item['count']

print(sum)