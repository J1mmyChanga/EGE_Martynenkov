from itertools import *

k = 0
for r in range(1, 11):
    for i in permutations('0123456789', r=r):
        if i[0] != '0' or len(i) == 1:
            if int(''.join(i)) % 5 == 0:
                k += 1
print(k)