def convert(n, k):
    s = ''
    alph = '0123456789abcdefghijklmnop'
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(17**5 + 85**8 - 10, 17)
print(n.count('g'))