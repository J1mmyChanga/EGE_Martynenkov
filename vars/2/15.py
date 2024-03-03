def f(x, y):
    return (y + 2*x != 48) or (a < x) or (a < y)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)