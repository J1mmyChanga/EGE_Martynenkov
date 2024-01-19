def convert(k):
    res = ''
    while k != 0:
        res += str(k % 5)
        k //= 5
    return res[::-1]

for n in range(1, 10000):
    dub = convert(n)
    if n % 25 == 0:
        dub += dub[-3:]
    else:
        dub += convert(n % 25)
    r = int(dub, 5)
    if r > 10000:
        print(n)
        break