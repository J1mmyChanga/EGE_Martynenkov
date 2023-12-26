alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338, 15)
print(len(set(n)))