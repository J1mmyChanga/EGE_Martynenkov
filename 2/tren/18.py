from itertools import *
c = 0

def f(x, y, z, w):
    return x and (y <= z) or w

s = set()
for item in product([0, 1], repeat=6):
    table = [(1, 0, item[0], 1), (item[1], 0, 1, item[2]), (item[3], 0, item[4], item[5])]
    if len(table) != len(set(table)):
        continue
    for p in permutations('xywz'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            s.add(p)
print(len(s))