for n in range(2, 2022):
    st = str(n)
    a = 0
    b = 0
    for i in range(len(st)):
        if int(st[i]) % 2 == 0:
            b += int(st[i])
        if i % 2 != 0:
            a += int(st[i])
    res = abs(b - a)
    if res == 9:
        print(n)