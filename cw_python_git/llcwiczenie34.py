def compare(obj1, obj2):
    return obj1 is obj2


print(compare("a", "b"))


#wcześniejsze wykonanie
'''
def f():
    x=input('wpisz jeden obiekt : ')
    print()
    y=input('wpisz drugi obiekt : ')
    print()
    print(x is y)

f()
f()
f()
f()
'''
