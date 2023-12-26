alph = '0123456789abcdefghijklmnop'
c = 0
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(1, 1000):
    if len(convert(n, 2)) >= 5 and len(convert(n, 5)) <= 4 and convert(n, 16).endswith('c'):
        c += 1
print(c)