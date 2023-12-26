alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(1, 1000):
    if len(convert(n, 6)) == 2 and len(convert(n, 5)) == 3 and convert(n, 11).endswith('1'):
        print(n)