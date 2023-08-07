

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.len

class Square:
    def __init__(self, a):
        self.side = a
    
    def calculate_perimeter(self):
        return 4 * self.side

prostokat = Rectangle(20,40)
kwadrat = Square(20)

print(prostokat.calculate_perimeter())
print(kwadrat.calculate_perimeter())



