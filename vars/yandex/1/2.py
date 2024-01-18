from itertools  import *
def f(a, b, c, d):
    return (a <= b) and (b <= c) and (c <= d)

for item in product([1, 0], repeat=2):
    table = [(0, item[0], 1, 0), (0, item[1], 1, 0), (0, 1, 1, 1)]
    if len(set(table)) != len(table):
        continue
    for i in permutations('abcd'):
        if [f(**dict(zip(i, row))) for row in table] == [1, 1, 1]:
            print(i)