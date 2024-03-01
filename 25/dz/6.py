def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for i in range(550001, 551000):
    d = f(i)
    if len(d) > 0 and int(sum(d)/len(d)) % 31 == 13:
        print(i, int(sum(d)/len(d)))