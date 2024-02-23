def reverse_iter(n):
    for i in range(n, -1, -1): 
        yield i

n = int(input())
for i in reverse_iter(n):
    print(i)