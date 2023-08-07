#moduł cubed'

# prosty sposób dla łatwiejszego zrozuminia
'''
def x():
    n=input('podaj liczbę:')
    n=int(n)
    n=n**3
    print(n)
'''

# trudniejszy z wyłapaniem błędu aby dobrze działał modół
# funkcja nie jest wywoływana w tym module , bo na końcu nie ma x(), dopiero
# w module drugim działa cubed2

def x():
    try:
        n=input('podaj liczbę:')
        n=int(n)
        n=n**3
        print(n)
    except ValueError:
        print('Niewłaściwe dane podaj liczbę')

