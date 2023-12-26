alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(1, 101):
    if len(str(n)) == 2 and convert(n, 16).endswith('a') and convert(n, 5).endswith('3'):
        print(n)