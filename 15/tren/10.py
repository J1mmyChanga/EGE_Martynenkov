def f(a, x, y, z):
    return (220 != y + 2 * x + z) or (a < 6 * x) or (a < 2 * z)

for a in range(1, 1000):
    if all(f(a, x, y, z) for x in range(150) for y in range(150) for z in range(150)):
        print(a) #119