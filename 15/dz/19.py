from itertools import combinations

def f(x):
    A = a1 <= x <= a2
    P = 17 <= x <= 54
    Q = 37 <= x <= 83
    return P <= ((Q and (not A)) <= (not P))

ox = [i/4 for i in range(17 * 4, 84 * 4)]
m = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(round(min(m)))