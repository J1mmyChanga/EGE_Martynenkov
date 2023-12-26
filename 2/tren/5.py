from itertools import product

print('x y z')
def f(x, y, z):
    return ((z or y) <= (x == z))

for x, y, z in product([0, 1], repeat=3):
    if not f(x, y, z):
        print(x, y, z) #yzx