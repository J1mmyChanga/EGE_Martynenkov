from itertools import *

def f(x):
    a = a1 <= x <= a2
    r = 1813 <= x <= 2566
    q = 1362 <= x <= 3898
    p = 1023 <= x <= 2148
    return (not (q <= (p or r))) <= ((not a) <= (not q))

ox = [x for x in range(1023, 3899)]
m = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)

# print(min(m)) - не рештл