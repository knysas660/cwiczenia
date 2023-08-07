#funkcja konwertująca łańcuch znaków na wartość typu float

try:
    
    """użytkownik wprowadza znaki"""
    a=input('podaj liczbę całkowitą lub dziesiętną(z kropką):')
    """tutaj przechwytuje błąd gdzie użytkownik może nie wpisać liczby"""
    a=float(a)
    """przkształca zmienną na zmienną przecinkową"""
    print('wynik konwersji:')
    print(a)
except ValueError:
    #robię odstęp
    print()
    """w wypadku błędu konwersji gdy urzytkownik wpisze litery,
    przecinki i inne znaki nie przedstawiające liczb wyświetli się
    komunikat"""
    
    print('niewłaściwe dane wejściowe: MUSI BYĆ JAKAŚ LICZBA ')




