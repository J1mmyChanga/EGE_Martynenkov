def convert(n, k=9):
    alph = '0123456789'
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]


for i in range(1, 10**9 + 1):
    b = str(convert(i))
    if sorted(str(b), reverse=True) == str(b):
        if b[0] == '3' and b[2:].startswith('458') and b[-1] == '3':
            print(i)