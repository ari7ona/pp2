import re

str = input()
pattern = '^a(b{2,3})$'

if re.search(pattern,  str):
    print('TRUE') 
else:
    print('FALSE')