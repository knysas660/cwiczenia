

class Hexagon:
    def __init__(self,a):
        self.bok=a

    def calkulate_perimeter(self):
        return 6 * self.bok

szesciokat=Hexagon(5)
print(szesciokat.calkulate_perimeter())
