
def f():
    
    print()
    n=input('Wprowadź  dane osobowe i inne jakie interesują cię o mnie :')

    dane={'wzrost':186,
          'kolor oczu':'zielony',
          'ulubiony autor':'Tolkien',
          'ulubiony kolor':'niebieski'}
    print()
    if n in dane:

        wartosc=dane[n]
        print(wartosc)

    else:
        print('Nie ma takich danych, wybierz inne')

f()
f()
f()
f()
f()
