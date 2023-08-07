# dwa nienajlepsze sposoby wyświetlenia listy z indeksami

lista=['Noc żywych trupów', 'Ekipa', 'Rodziny Soprano', 'Pamiętniki wampirów']

'''
for i , show in enumerate(lista):
    new=lista[i]
    new=str(i)+' '+new
    print(new)
'''    


i=0
for show in lista:
    new=lista[i]
    new=str(i)+' '+new
    print(new)
    i+=1
    
