alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(3*16**8 - 4**5 + 3, 4)
print(n.count('3'))