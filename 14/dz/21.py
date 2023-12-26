alph = '0123456789abcdefghijklmnop'
c = 0
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 17):
    n = int(f'9759{alph[x]}', 17) + int(f'3{alph[x]}108', 17)
    if n % 11 == 0:
        print(n / 11)