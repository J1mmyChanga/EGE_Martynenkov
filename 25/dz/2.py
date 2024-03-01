def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(81234, 134690):
    a = f(i)
    if len(a) == 3:
        print(a[0], a[1], a[2])