#!/usr/bin/python3

import re

string = 'Bieg na orientację dookoła miejskiego zoo.'

m = re.findall('.oo',
               string,
               re.IGNORECASE)

print(m)


