from itertools import *
c = 0

def f(p1, p2, p3, p4):
    return (p3 <= p1) <= (p4 or (not p2))

for item in product([0, 1], repeat=4):
    table = [(0, 0, item[0], 1), (0, 1, item[1], 1), (1, 1, item[2], item[3])]
    if len(table) != len(set(table)):
        continue
    for p in permutations(['p1', 'p2', 'p3', 'p4']):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)