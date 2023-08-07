
class Shape():
    def __init__(self):
        pass
    
    def what_am_i(self):
        print('Jestem figurą')    

#my=Shape()
#my.what_am_i()
#jeśli wpiszę print(my.what_am_i()) to funkcja będzie miała dodatkową wartość
# None, ponieważ utworzy się postać   print(print('Jestem figurą'))

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.len

class Square(Shape):
    
    def __init__(self, a):
        self.side = a
    
    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, b):
        self.side = b+self.side

prostokat = Rectangle(20,40)
kwadrat = Square(20)


prostokat.what_am_i()
#jeśli wpiszę print(prostokąt.what_am_i()) to funkcja będzie miała
# dodatkową wartość
# None, ponieważ utworzy się postać   print(print('Jestem figurą'))

print(prostokat.calculate_perimeter())

kwadrat.what_am_i()
#jeśli wpiszę print(kwadrat.what_am_i()) to funkcja będzie miała
# dodatkową wartość
# None, ponieważ utworzy się postać   print(print('Jestem figurą'))

print(kwadrat.calculate_perimeter())


