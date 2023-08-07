#python_lst258.py

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print('''{} na {}'''
              .format(self.width,
                      self.len))

my_shape = Shape(20,20)
my_shape.print_size()
