def convert(n, k):
    s = ''
    alph = '0123456789abcdefghijklmnop'
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(7**103 + 6 * 7**104 - 3 * 7**57 + 98, 7)
print(sum([int(i) for i in n]))