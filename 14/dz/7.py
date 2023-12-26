alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024, 25)
print(n.count('0'))