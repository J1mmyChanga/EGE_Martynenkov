from itertools import *
def f(w, x, y, z):
    return (w or x or y) <= ((y or z) and x or y and (w or z))

for i in product([0, 1], repeat=5):
    table = [(0, 0, 0, i[0]), (i[1], 1, 1, i[2]), (i[3], 1, i[4], 1)]
    if len(table) != len(set(table)):
        continue
    for a in permutations('xyzw'):
        if [f(**dict(zip(a, row))) for row in table] == [0, 0, 0]:
            print(a)