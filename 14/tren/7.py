def convert(n, k):
    s = ''
    alph = '0123456789abcdefghijklmnop'
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(100):
    n = [int(i) for i in convert(81**20 - 9**x + 50, 9)]
    if sum(n) == 138:
        print(x)
        break