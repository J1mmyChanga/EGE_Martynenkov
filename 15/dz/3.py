def f(a, x):
    return ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0))

for a in range(1, 100000):
    if all(f(a, x) for x in range(1, 1000000)):
        print(a)
        break #7