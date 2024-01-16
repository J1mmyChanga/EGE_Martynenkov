from fnmatch import fnmatch

res = {}

def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def have4dels(n):
    c = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i):
            c += 1
            if c == 5:
                break
    return c > 4

for i in range(34089, 10 ** 7 + 1):
    if fnmatch(str(i), '34?8*9') and have4dels(i):
        print(i)