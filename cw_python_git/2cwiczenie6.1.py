
def powtorka_programu():

    
    try:
        
        def f1():
            a=input('podaj liczbę całkowitą (dziesiątki nie zostaną uwzględnione):')
            a=int(a)
            return a/2
        
        #robię odstęp
        print()
        
        z=f1()
        #robię odstęp
        print()
        
        print('wynik pierwszej funkcji dzielienia przez 2:')
        #robię odstęp:
        print()
        
        print(z)
        #robię odstęp print():
        print()

        def f2(z):
            return z*4
        print('wynik drugiej funkcji mnożenia wyniku przez 4 z pierwszego dzielenia:')
        #robię odstęp
        print()
        
        print(f2(z))
    except ValueError:
        #robię odstęp
        print()
        print('niewłaściwe dane wejściowe: MUSISZ PODAĆ LICZBĘ')

powtorka_programu()
powtorka_programu()
powtorka_programu()
powtorka_programu()
