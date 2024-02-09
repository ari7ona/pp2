import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers_str):
    numbers = list(map(int, numbers_str.split()))
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

result = filter_prime('5 2 25 12 3 6')
print(result)