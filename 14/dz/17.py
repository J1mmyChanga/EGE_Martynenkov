alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(2, 30):
    if convert(68, n).endswith('2') and len(convert(68, n)) == 4:
        print(n)