#słownik kojarzący ulubionych muzyków z ich utworami

def f():
    
    lista1=[1,2,3,4]

    lista2=[1,2,3,4,5,6]

    lista3=[1,2,3]

    muzycy={'Michael Oldfild':lista1,'Vangelis':lista2,'ACDC':lista3}
    print()
    n=input('wpisz mojego ulubionego muzyka lub zespół aby wyświetlić jego\
 utwory  (m.in.Michael Oldfild,Vangelis,ACDC    : ')
    print()

    if n in muzycy:
        print(muzycy[n])

    else:
        print(' Nie ma takiego mojego ulubionego muzyka, zesołu lub nazwa jest\
 źle wpisana(może być z imieniem).')

f()
f()
f()
f()
