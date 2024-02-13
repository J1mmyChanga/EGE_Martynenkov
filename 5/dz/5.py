def convert(n):
    res = ''
    while n != 0:
        res = str(n % 3) + res
        n //= 3
    return res

for n in range(1, 100):
    st = convert(n)
    st += str(n % 3)
    print(n, int(st, 3))