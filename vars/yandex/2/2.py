from itertools import *

def f(a, b, c, d):
    return ((a and b) <= c) and ((b and c) <= d)

for a in product([0,1], repeat=6):
    table = [(a[0], 1, 1, 1), (a[1], 1, a[2], 1), (1, 1, 1, a[3]), (a[4], 1, 1, a[5])]
    if len(table) != len(set(table)):
        continue
    for i in permutations('abcd'):
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0, 0]:
            print(i)