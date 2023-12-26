from itertools import product, permutations

def f(a, b, c):
    return (a and (not c)) or ((not b) and (not c))

table = [(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (0, 1, 1, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 1, 0, 1), (1, 1, 1, 0)]
for p in permutations('abc'):
    if [f(**dict(zip(p, row))) for row in table] == [1, 0, 0, 0, 1, 0, 1, 0]:
        print(p)