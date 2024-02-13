for n in range(1000, 10000):
    st = str(n)
    a = int(st[0]) * int(st[1])
    b = int(st[2]) * int(st[3])
    if a < b:
        res = f'{a}{b}'
    else:
        res = f'{b}{a}'
    if res == '1214':
        print(n)