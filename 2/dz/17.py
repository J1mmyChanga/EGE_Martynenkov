from itertools import product, permutations

def f(a, b, c, d):
    return ((not a) and (not b)) or (b == c) or d

for item in product([0, 1], repeat=4):
    table = [(item[0], item[1], 1, item[2]), (1, 0, item[3], 1), (0, 0, 1, 1)]
    if len(set(table)) != len(table):
        continue
    for p in permutations('abcd'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)