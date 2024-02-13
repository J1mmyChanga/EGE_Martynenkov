a = []
for n in range(300, 401):
    st = str(n)
    sp = [st[0] + st[1], st[0] + st[2], st[1] + st[0], st[1] + st[2], st[2] + st[1], st[2] + st[0]]
    mas = [int(i) for i in sp if i[0] != '0']
    if max(mas) - min(mas) == 20:
        a.append(n)
print(len(a))