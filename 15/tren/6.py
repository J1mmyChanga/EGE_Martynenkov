def f(a, x):
    return (x & a == 0) and (x & 41 != 0) and (x & 33 == 0)

for a in range(1, 10000):
    if all((not f(a, x)) for x in range(1, 1000000)):
        print(a) #8
        break