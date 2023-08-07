#!/usr/bin/python3
#python_lst286.py

import re

line = 'Kocham $'

m = re.findall('\\$',
               line,
               re.IGNORECASE)

print(m)

