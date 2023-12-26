alph = '0123456789abcdefghijklmnop'
c = 0
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 15):
    for y in range(1, 17):
        n = int(f'123{alph[x]}5', 15) + int(f'67{alph[y]}9', 17)
        if n % 131 == 0:
            print(n / 131, x, y)