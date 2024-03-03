for n in range(1, 5000):
    st = bin(n)[2:]
    if n % 2 == 0:
        st += st[-2] + st[-1]
    else:
        st = '1' + st + '1'
    print(n, int(st, 2))