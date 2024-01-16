def f(x):
    A = x in a
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    R = x in {12, 24, 36, 48, 60}
    return (not A) <= ((P and Q) <= R)

a = []
for x in range(1, 100000):
    if not f(x):
        print(x) #648