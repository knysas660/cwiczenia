#python_lst153.py

rhymes={'1':'niebem',
        '2':'kwa kwa',
        '3':'śni',
        '4':'ordery',
        '5':'cięć'
        }

n=input('Wpisz cyfrę :  ')
if n in rhymes:
    rhyme=rhymes[n]
    print(rhyme)
else:
    print('Nie znaleziono.')
