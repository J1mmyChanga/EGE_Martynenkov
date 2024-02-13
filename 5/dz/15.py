for n in range(100, 1000):
    st = str(n)
    a = int(st[0]) * int(st[1])
    b = int(st[2]) * int(st[1])
    if a > b:
        res = f'{a}{b}'
    else:
        res = f'{b}{a}'
    if res == '240':
        print(n)