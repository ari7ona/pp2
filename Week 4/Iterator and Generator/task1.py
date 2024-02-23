def squ_gen(n):
    for i in range(n):
        yield i**2

n = int(input())
squares = squ_gen(n)
for square in squares:
    print(square)