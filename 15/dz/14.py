def f(x):
    A = x in a
    B = x in {1, 3, 5, 7, 9, 11}
    C = x in {3, 6, 9, 12}
    return (B <= (not C)) or A

a = []
for x in range(1, 100000):
    if not f(x):
        print(x) #12