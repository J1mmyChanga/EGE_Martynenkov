alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(7, 22):
    if convert(56, n)[-1] == '1' and convert(45, n)[-1] == '1':
        print(n)