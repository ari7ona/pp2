def even_gen(n):
    for i in range(0, n + 1, 2): 
        yield i

n = int(input())
for i in even_gen(n):
    if i < n - 1:
        print(i, end = ', ')
    else:
        print(i)