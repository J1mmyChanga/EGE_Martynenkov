for n in range(100, 1000):
    st = str(n)
    sp = [st[0] + st[1], st[1] + st[2]]
    mas = [int(i) for i in sp]
    res = max(mas) - min(mas)
    if res == 44:
        print(n)