alph = '0123456789abcdefghijklmnop'
c = 0
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 15):
    n = int(f'123{alph[x]}5', 15) + int(f'1{alph[x]}233', 15)
    if n % 14 == 0:
        print(n / 14)