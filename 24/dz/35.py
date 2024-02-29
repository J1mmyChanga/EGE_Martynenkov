from itertools import *

s = open('files/24_2501.txt').readline()
k = 0
for i in range(4, len(s)):
    if s[i-4] == s[i-2] == s[i] == 'A':
        k += 1
print(k)