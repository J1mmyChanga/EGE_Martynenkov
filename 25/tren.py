def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

a = int(input("Enter a number: "))
print(IsPrime(a))