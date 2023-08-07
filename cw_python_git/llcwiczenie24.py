

class Horse:
    def __init__(self,
                 i,
                 r,
                 j):
        self.imie = i
        self.rasa = r
        self.jezdziec = j

class Rider:
    def __init__(self, i):
        self.imie = i

jokey = Rider('Lukas')
kon = Horse('Szybki',
            'arab',
            jokey)

print(kon.jezdziec.imie)
