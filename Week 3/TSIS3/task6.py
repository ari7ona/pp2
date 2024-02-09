numbers = [5, 2, 25, 12, 3, 6]

for i in range(2, int(max(numbers)**0.5) + 1):
    numbers = list(filter(lambda n: n == i or n % i != 0 and not n == 1, numbers))

print(numbers)