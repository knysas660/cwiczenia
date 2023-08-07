
lista=[4,5,8,10,12]
while True:
    try:
        
        x=input('odgadnij liczbę całkowitą listy od 0 do 15 \n \
        (chcesz przerwać wpisz q ):')
        print()
        if x=='q':
            break
        x=int(x)
    except ValueError:
        print('Niewłaściwe dane wpisz liczbę lub q\n ')
        continue
    if x in lista:
        print('zgadłeś, próbuj dalej')
        print()
    else:
        print('nie zgadłeś, póbuj dalej')
        print()
