import math

n_sides = int(input('Input number of sides: '))
side_length = int(input('Input the length of a side: '))

perimeter = n_sides * side_length
apothem = side_length / (2 * math.tan(math.radians(180) / n_sides))

print('Area of polygon:', round(perimeter * apothem / 2))