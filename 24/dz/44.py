from string import *

s = open('files/24_2505.txt').readline()
d = {x:0 for x in ascii_uppercase}

for i in range(1, len(s)-1):
    if s[i-1] == s[i+1]:
        d[s[i]] += 1
for i in d:
    if d[i] == max(d.values()):
        print(i+str(d[i]))