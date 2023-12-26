alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(8, 25):
    if int('103', x) == int('97', x + 2):
        print(x)
        break