from itertools import *

def f(x):
    A = a1 <= x <= a2
    P = 25 <= x <= 37
    Q = 32 <= x <= 50
    return (A and (not Q)) <= (P or Q)

ox = [i / 4 for i in range(24 * 4, 51 * 4)]
m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(max(m)) #25