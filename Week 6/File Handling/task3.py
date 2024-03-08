import os

path = '/Users/azhexenbekov/'

if os.path.exists(path):
    print(os.listdir(path))
else:
    print('Path does not exists')