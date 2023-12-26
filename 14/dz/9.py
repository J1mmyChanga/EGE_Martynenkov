alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 102):
    n = [int(i) for i in convert(36**17 - 6**x + 71, 6)]
    if sum(n) == 61:
        print(x)
        break