#python_lst37.py

colors=['niebieski','zielony','czerwony']

guess=input('Zgadnij, jaki kolor wybrałem?(pisz małymi literami):')
print()
if guess in colors:
    print('Zgadłeś!')
else:
    print('Źle, spróbuj jeszcze raz.')
