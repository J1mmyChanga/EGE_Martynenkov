from string import *

k = 0
s = open('files/24_2508.txt').readlines()
num = max(i.count('Q') for i in s)

for i in s:
    if i.count('Q') == num:
        st = i
d = {x:0 for x in ascii_uppercase}

for i in st.strip():
    d[i] += 1

if 0 in d.values():
    min_k = sorted(set(d.values()))[1]
else:
    min_k = sorted(set(d.values()))[0]

for i in d:
    if d[i] == min_k:
        print(i)

for i in s:
    k += i.count('C')
print(f'C{k}')