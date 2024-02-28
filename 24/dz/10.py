from itertools import *
s = open('files/24_8510.txt').readline()
# m = [1] * len(s)
# for i in range(1, len(s)):
#     if (s[i-1], s[i]) not in product('NOP', repeat=2):
#         m[i] = m[i-1] + 1
# print(max(m))

s = s.replace('N', 'P').replace('O', 'P')
while 'PP' in s:
    s = s.replace('PP', 'P P')
print(max(len(c) for c in s.split()))