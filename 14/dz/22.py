alph = '0123456789abcdefghijklmnop'
c = 0
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 11):
    n = int(f'3364{alph[x]}', 11) + int(f'{alph[x]}7946', 12)
    if n == int(f'55{alph[x]}87', 14):
        print(int(f'55{alph[x]}87', 14))