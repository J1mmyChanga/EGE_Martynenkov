def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

def p(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

for i in range(125697, 125722):
    d = [x for x in f(i) if p(x)]
    if len(d) == 2 and d[0] * d[1] == i:
        print(d[0], d[1])