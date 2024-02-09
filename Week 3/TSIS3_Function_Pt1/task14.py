from task1 import convert
from task11 import is_palindrome
from task12 import histogram

#Task1
def convert(weight):
    weight = weight * 28.3495231
    return weight

print(convert(5))

#Task11
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else: return False

print(is_palindrome('qyryq'))

#Task12
def histogram(list):
    hg_list = []
    for i in list:
        hg_list.append(i*('*'))
    return ' '.join(hg_list[0::])

print(histogram([4, 9, 7]))