alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(2*27**7 + 3**10 - 9, 3)
print(n.count('0'))