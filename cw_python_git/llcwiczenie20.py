#python_lst262.py

class Dog():
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person():
    def __init__(self,name):
        self.name = name

#python_lst263.py

#dalszy ciąg
#poprzedniego przykładu

mick = Person('Mick Jagger')
stan = Dog('Stanley',
           'Bulldog',
           mick)

print(stan.owner.name)
