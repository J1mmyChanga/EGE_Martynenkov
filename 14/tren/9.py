alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(19):
    n = int(f'9009{alph[x]}', 18) + int(f'2257{alph[x]}', 18)
    if n % 15 == 0:
        print(n / 15)
        break