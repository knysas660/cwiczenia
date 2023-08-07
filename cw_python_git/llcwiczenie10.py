

class Tringle:
    def __init__(self,a,h):
        self.podstawa=a
        self.wysokosc=h

    def area(self):
        return 1/2 * self.podstawa * self.wysokosc

trojkat=Tringle(5, 10)
print(trojkat.area())
