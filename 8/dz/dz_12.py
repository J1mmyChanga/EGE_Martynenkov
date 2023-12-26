from itertools import *


a = []
for i in product('ABCD', repeat=4):
    s = ''.join(i)
    if s[0] <= s[1] <= s[2] <= s[3]:
        print(s)
        a.append(s)
print(len(a))