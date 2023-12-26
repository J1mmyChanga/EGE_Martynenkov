alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(4, 25):
    if int('132', x) + int('13', 8) == int('124', x + 1):
        print(x)
        break