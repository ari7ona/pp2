class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

s = Shape()
print (s.area())

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

r = Rectangle(5, 10)
print(r.area())