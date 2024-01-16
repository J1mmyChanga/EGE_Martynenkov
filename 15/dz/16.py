def f(x):
    A = x in a
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
    return (A <= P) and (Q <= (not A))

a = list(range(1, 10000))
for x in range(1, 10000):
    if not f(x):
        a.remove(x)
print(a) #8