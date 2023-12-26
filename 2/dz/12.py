from itertools import product, permutations

def f(x, y, z, w):
    return (not w) and ((y or z) <= ((not x) and y))

for item in product([0, 1], repeat=8):
    table = [(item[0], item[1], item[2], 1), (item[3], item[4], 1, item[5]), (item[6], 1, 1, item[7])]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
            print(p)