from itertools import *
c = 0
def f(x, y, w, z):
    return (x == y) <= (z == w)

table = [(0, 0, 0, 1), (1, 1, 1, 0)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, row))) for row in table] == [0, 0]:
        c += 1
print(c)