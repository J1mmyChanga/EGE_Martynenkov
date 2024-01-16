from itertools import *

def f(x):
    A = a1 <= x <= a2
    P = 5 <= x <= 100
    Q = 15 <= x <= 25
    R = 35 <= x <= 50
    return (P <= Q) or ((not A) <= R)

ox = [i / 4 for i in range(5 * 4, 101 * 4)]
m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(min(m)) #95