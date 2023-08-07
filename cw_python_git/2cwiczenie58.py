# program pyta o ulubione miesiące i po tym jak odpowiadamy
# wprowadza tą odpowiedź i zapisuje w pliku(jeśli go nie ma to tworzy nowy)
# cudowny.txt na pulpicie

x=input('Jakie miesiące w roku są twoimi ulubionymi ?')

import os

plik=os.path.join('C:\\',
	     'Users',
	     'euro',
	     'Desktop',
	     'cudowny.txt')

with open(plik, 'w') as f:
    f.write(x)

print('Twoja odpowiedź została zapisana w pliku tekstowym:\n\n cudowny.txt \
        na pulpicie komputera. Skasuj sobie go ')
