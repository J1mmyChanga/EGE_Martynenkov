def f(x):
    A = x in a
    B = x in {-42, -10, -8, 2, 16}
    C = x in {-10, -4, 2, 15, 23}
    return (A <= B) or C

a = list(range(0, 100000))
for x in range(0, 100000):
    if not f(x):
        a.remove(x)
print(a)
print(sum(a))