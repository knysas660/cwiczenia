

class Circle:
    def __init__(self,r):
        self.promien=r
        import math
        self.pi=math.pi

    def area(self):
        return self.pi * self.promien ** 2

kolo=Circle(5)
print(kolo.area())
