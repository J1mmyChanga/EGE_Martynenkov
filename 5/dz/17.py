for n in range(100, 1000):
    st = str(n)
    sp = [st[0] + st[1], st[0] + st[2], st[1] + st[0], st[1] + st[2], st[2] + st[1], st[2] + st[0]]
    mas = [int(i) for i in sp if i[0] != '0']
    if max(mas) - min(mas) == 5:
        print(n)