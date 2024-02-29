import string
from string import *

s = open('files/24_2506.txt').readline()
d = {x:0 for x in string.ascii_uppercase}
for i in s.strip():
    d[i] += 1
print(max(d.values()))
for i in d:
    if d[i] == max(d.values()):
        print(i)
        break