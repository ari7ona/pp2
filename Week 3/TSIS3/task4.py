import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, p):
        return math.sqrt((p.x - self.x)**2 + (p.y - self.x)**2)

p1 = Point(3, 5)
print('First point coordinates:', p1.show())

p2 = Point(1, 2)
print('Second point coordinates:', p2.show())

p1.move(4, 1)
print('First point moved coordinates:', p1.show())

print('Distance between two points:', p1.dist(p2))