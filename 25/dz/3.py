def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(154026, 154043):
    a = f(i)
    if len(a) == 4:
        print(a[2], a[3])