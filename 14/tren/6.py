def convert(n, k):
    s = ''
    alph = '0123456789abcdefghijklmnop'
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(7**2 + 49**4 - 21, 14)
print(n.count('0') + n.count('a'))