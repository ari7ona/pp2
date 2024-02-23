def dev34_gen(n):
    for i in range(n): 
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for i in dev34_gen(n):
    if i < n - 1:
        print(i, end = ', ')
    else:
        print(i)