def convert(n, k):
    s = ''
    alph = '0123456789abcdefghijklmnop'
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 1000):
    n = convert(64**12 - 8**14 + x, 8)
    if n.count('7') == 12 and n.count('1') == 1:
        print(x)
        break