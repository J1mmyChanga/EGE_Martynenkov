alph = '0123456789abcdefghijklmnop'
a = []
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(1, 51):
    if convert(n, 3).endswith('21'):
        a.append(n)
print(len(a))