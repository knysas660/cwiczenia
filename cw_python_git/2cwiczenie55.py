#python_lst234.py

import csv

with open('st.csv','w',newline='') as f:
    write = csv.writer(f,delimiter=',')
    write.writerow(['jeden',
                    'dwa',
                    'trzy'])
    write.writerow(['cztery',
                    'pięć',
                    'sześć'])
    
