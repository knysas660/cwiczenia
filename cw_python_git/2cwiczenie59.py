#lista_list ma być zapisana w piku csv dla excla lub
#innych arkuszy kalkulacyjnych

lista_list=[['Top Gun','Ocean\'s Eleven','Raport mniejszości'],
            ['Titanic','Ostatni Jedi','Incepcja'],
            ['Pulp Fiction','Człowiek w ogniu','Seksmisja']]

#potrzebny moduł os z funkcją path do określenia lokalizacji nowego pliku
# i jego nazwy

# do otworzenia pliku csv  używamy instrukcji   with
# wewnątrz niej trzeba korzystać z modułu csv aby skonwertować
#obiekt pliku na csv


#potrzebny moduł csv do utworzenia pliku z rozszerzeniem .csv
# z metodą   writer   każdy element będzie oddzielony separatorem w wywołaniu
# metoda   writerow   tworzy tylko jeden wiersz dlatego trzeba było
# wywołać ją trzykrotnie


import os
import csv

plik=os.path.join('C:\\',
	     'Users',
	     'euro',
	     'Desktop',
	     'excelplik.csv')

with open(plik, 'w', newline='') as f:
    write = csv.writer(f, delimiter=',')
    write.writerow(lista_list[0])
    write.writerow(lista_list[1])
    write.writerow(lista_list[2])

print('Twoja lista list została zapisana w pliku do excela:\n\n excelplik.csv \
        na pulpicie komputera. Skasuj sobie go ')
