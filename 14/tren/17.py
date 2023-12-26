alph = '0123456789abcdefghijklmnop'
a = []
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(1, 101):
    if convert(n, 16).endswith('c'):
        a.append(n)
print(len(a))