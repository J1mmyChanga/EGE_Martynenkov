for n in range(1, 150):
    st = bin(n)[2:]
    if n % 2 == 0: st += '01'
    else: st += '10'
    print(n, int(st, 2))