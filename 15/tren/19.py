from itertools import *

def f(x):
    A = a1 <= x <= a2
    P = 2 <= x <= 20
    Q = 15 <= x <= 25
    return ((not A) <= (not P)) or Q

ox = [i / 4 for i in range(2 * 4, 26 * 4)]
m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(min(m)) #13