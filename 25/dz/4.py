def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(150001, 150900):
    d = f(i)
    if len(d) > 0 and sum(d) % 13 == 10:
        print(i, sum(d))