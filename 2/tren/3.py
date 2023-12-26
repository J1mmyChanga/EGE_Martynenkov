from itertools import product

print('x y z')
def f(x, y, z):
    return (not(z) and x) or (x and y)

for x, y, z in product([0, 1], repeat=3):
    print(x, y, z, f(x, y, z)) #zyx