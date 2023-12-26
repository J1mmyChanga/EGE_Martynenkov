alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for n in range(7, 30):
    if int('154', n)  + int('35', 9) == int('170', n + 1):
        print(n)