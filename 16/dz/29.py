def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 2*f(n-1)

# for i in range(1,20):
#     print(i, bin(i)[2:], f(i))

print(2**1900/2**1890)