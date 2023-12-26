alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(4, 25):
    if int('33', x+4) - int('33', 4) == int('33', 10):
        print(x)
        break