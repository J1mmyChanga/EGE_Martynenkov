alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(7, 33):
    if convert(338, n)[-1] == '2' and len(convert(338, n)) == 3:
        print(n)