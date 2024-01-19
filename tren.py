def convert(n):
    res = ''
    while n != 0:
        res += str(n % 4)
        n //= 4
    return res[::-1]

for n in range(1, 10000):
    dub = convert(n)
    if len(dub) % 2 == 0:
        dub = dub[:len(dub) // 2] + '0' + dub[len(dub) // 2:]
    if int(dub) <= 180:
        print(n)