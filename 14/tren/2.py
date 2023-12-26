def convert(n, k):
    s = ''
    while n != 0:
        s += str(n % k)
        n //= k
    return s[::-1]

n = convert(7**103 + 20 * 7**204 - 3 * 7**57 + 97, 7)
print(n.count('6'))