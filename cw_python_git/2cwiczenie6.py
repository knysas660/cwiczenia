#funkcja, która ma trzy wymagane parametry i dwa opcjonalne



def f(x,y,z,a=1,b=2):
    return (x+y+z)-a*b


print(f(1,5,8))
#robię odstęp print():
print()
#wpisuję wszystkie parametry:
print(f(1,5,8,4,8))
