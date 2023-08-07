#!/usr/bin/python3

import re

line =' Arizona 479, 501, 870. California 209, 213, 650.'


m = re.findall('\d',
               line,
               re.IGNORECASE)

print(m)

