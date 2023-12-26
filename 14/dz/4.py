alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = [int(i) for i in convert(51*7**12 - 7**3 - 22, 7)]
print(sum(n))