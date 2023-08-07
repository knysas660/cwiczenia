#python_lst250.py

class Orange():
    def __init__(self,w,c):
        '''waga podawana jest w gramach'''
        self.weight = w
        self.color = c
        self.mold = 0
        print('Utworzono!')

    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(170, 'pomarańczowy')
print(orange.mold)
orange.rot(10, 29)
print(orange.mold)
