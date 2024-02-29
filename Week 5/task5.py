import re

str = input()
pattern = 'a.*b$'

if re.search(pattern,  str):
    print('TRUE') 
else:
    print('FALSE')