from itertools import *

def f(x):
    A = a1 <= x <= a2
    P = 1 <= x <= 98
    Q = 25 <= x <= 42
    return Q <= (((not P) and Q) <= A)

ox = [i / 4 for i in range(1 * 4, 99 * 4)]
m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(round(min(m))) #0