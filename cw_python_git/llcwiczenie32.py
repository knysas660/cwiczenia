
class Square:
    square_list=[]
    
    def __init__(self, a):
        self.bok_kwadratu=a
        self.square_list.append(self.bok_kwadratu)

k = Square(4)
k2 = Square(9)
print(Square.square_list)
        
