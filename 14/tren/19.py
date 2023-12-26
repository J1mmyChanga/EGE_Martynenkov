alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(100000):
    if len(convert(n, 3)) == 4 and len(convert(n, 7)) == 3 and convert(n, 8).endswith('17'):
        print(n)