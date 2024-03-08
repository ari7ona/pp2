import os

to_write = ['1', '2', '3']

with open('./task5.txt', 'w+') as file:
    for i in to_write:
        file.write('%s\n' %i)

file.close()