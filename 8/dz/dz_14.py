from itertools import *


a = []
for i in product('0123456789', repeat=3):
    s = ''.join(i)
    if s[0] != '0':
        if s[0] <= s[1] <= s[2]:
            print(s)
            a.append(s)
print(len(a))