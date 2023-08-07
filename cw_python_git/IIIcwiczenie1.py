#!/usr/bin/python3
import re
t='__jeden__ __dwa__ __trzy__ __cztery__ __pięć__'
results = re.findall('__.*?__',t)

for match in results:
    print(match)

