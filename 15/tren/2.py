def f(a, x):
    return ((x % 34 == 0) and (x % 51 != 0)) <= ((x % a != 0) or (x % 51 == 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 10000)):
        print(a) #3