alph = '0123456789abcdefghijklmnop'
c = 0
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 21):
    for y in range(1, 21):
        n = int(f'12{alph[y]}{alph[x]}9', 21) + int(f'36{alph[y]}99', 21)
        if n % 18 == 0:
            print(47594 / 18, x, y)