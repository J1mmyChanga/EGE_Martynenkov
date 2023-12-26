from itertools import product

print('x y z')
def f(x, y, z):
    return (x <= y) and (y <= z)

for x, y, z in product([0, 1], repeat=3):
    if f(x, y, z):
        print(x, y, z) #zxy