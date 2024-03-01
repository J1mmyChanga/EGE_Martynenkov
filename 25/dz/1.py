def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

d = {}
for i in range(174457, 174505+1):
    a = f(i)
    if len(a) == 2:
        d[f'{a[0]} {a[1]}'] = a[0]*a[1]
for i in sorted(d, key=lambda x:d[x]):
    print(i)