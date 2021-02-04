# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 15:12:50 2020

@author: Eilder Jorge
"""

import re
print(sum((int(y) for y in (re.findall("[0-9]+", open("D:\\regex_sum_42.txt").read())))))