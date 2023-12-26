alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

for x in range(1, 1001):
    n = convert(125**200 - 5**x + 74, 5)
    if n.count('4') == 100:
        print(x)
        break