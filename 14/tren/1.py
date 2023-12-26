def convert(n, k):
    s = ''
    while n != 0:
        s += str(n % k)
        n //= k
    return s[::-1]

c = 0
for i in range(2, 11):
    flag = True
    for j in convert(3456, i):
        if int(j) % 2 != 0:
            flag = False
            break
    if flag:
        c += i
print(c)