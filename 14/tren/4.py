def convert(n, k):
    s = ''
    alph = '0123456789abcdefghijklmnop'
    while n != 0:
        s += alph[n % k]
        n //= k
    return s[::-1]

n = convert(6**203 + 5 * 6**405 - 3 * 6**144 + 76, 6)
print(n.count('0') - n.count('5'))