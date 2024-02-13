for n in range(1, 10000):
    ed = 0
    nuls = 0
    st = bin(n)[2:]
    for i in range(1, len(st)):
        if i % 2 != 0 and st[i] == '1':
            ed += 1
        elif i % 2 == 0 and st[i] == '0':
            nuls += 1
    if abs(ed - nuls) == 5:
        print(n)
    # print(n, abs(ed - nuls))