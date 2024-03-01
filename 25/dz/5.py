def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(250201, 251000):
    d = f(i)
    if len(d) > 0 and (max(d) + min(d)) % 123 == 17:
        print(i, max(d) + min(d))