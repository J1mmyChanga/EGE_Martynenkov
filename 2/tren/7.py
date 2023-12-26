from itertools import product

print('x y z w')
def f(x, y, z, w):
    return (x == (not(z))) <= ((x or w) == y)

for x, y, z, w in product([0, 1], repeat=4):
    if not f(x, y, z, w):
        print(x, y, z, w) #xwyz