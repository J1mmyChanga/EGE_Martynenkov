a = 'КАРА'
k = 1
i = len(a)
b = 'Т'
while i > 1:
    c = a[i - 1]
    b += c
    i -= k
print(b)