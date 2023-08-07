# odczytuję plik moto.txt w laptopie na pulpicie jeśli dalej tam będzie
# program automatycznie zamyka go

import os

# w ścieżce dostępu na początku dysku C po dwukropku
# musi być podwójny odwrotny ukośnik.
# Jeden zapobiega odczytanie znaku specjalnego czyli \ który zapobiegałby
# apostrofowi lub cudzysłowiu  dlatego musi być \\

x=os.path.join('C:\\',
	     'Users',
	     'euro',
	     'Desktop',
	     'moto.txt')

with open(x, 'r') as f:
    print(f.read())
    
