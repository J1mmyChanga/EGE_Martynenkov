from itertools import combinations

def f(x):
    A = a1 <= x <= a2
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    return (B <= A) and ((not C) or A)

ox = [i / 4 for i in range(16 * 4, 53 * 4)]
m = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(round(min(m))) #36