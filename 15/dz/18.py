from itertools import *
def f(x):
    A = a1 <= x <= a2
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    return D <= (((not C) and (not A)) <= (not D))

ox = [i/4 for i in range(17 * 4, 81 * 4)]
m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(round(min(m))) #12