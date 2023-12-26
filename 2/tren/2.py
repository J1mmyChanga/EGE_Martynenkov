from itertools import product

print('x y z w')
def f(x, y, z, w):
    return not(w) and z and (y <= x)

for x, y, z, w in product([0, 1], repeat=4):
    if f(x, y, z, w):
        print(x, y, z, w) #zwxy