alph = '0123456789abcdefghijklmnop'
def convert(n, k):
    s = ''
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(5*216**1156 - 4*36**1147 + 6**1153 - 875, 6)
print(n.count('5') - n.count('0'))