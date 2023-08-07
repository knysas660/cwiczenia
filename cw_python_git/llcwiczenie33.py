
class Square:
    boki_obiektow=[]
    
    def __init__(self, a):
        self.bok_kwadratu=a
        self.boki_obiektow.append(self.bok_kwadratu)
        print('''{} na {} na {} na{}'''
              .format(self.bok_kwadratu,
                      self.bok_kwadratu,
                      self.bok_kwadratu,
                      self.bok_kwadratu))


k = Square(4)
k2 = Square(9)
print(Square.boki_obiektow)


