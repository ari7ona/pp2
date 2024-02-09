class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

s = Shape()
print (s.area())

class Square(Shape):
    def __init__(self, length = 0):
        self.length = length
    def area(self):
        return self.length**2

sq = Square(5)
print(sq.area())