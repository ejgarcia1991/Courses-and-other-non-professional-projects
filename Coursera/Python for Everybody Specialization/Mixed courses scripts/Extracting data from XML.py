# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:53:46 2020

@author: Eilder Jorge
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = ('http://py4e-data.dr-chuck.net/comments_768126.xml')
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
sum=0
for c in tree.iter('count'):
    sum+=int(c.text)
print(sum)