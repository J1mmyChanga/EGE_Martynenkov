alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(4, 25):
    if int('21', x) * int('13', x) == int('313', x):
        print(x)
        break