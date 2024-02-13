mas = []
for n in range(1, 100):
    st = bin(n)[2:]
    if n % 2 == 0: st = '1' + st + '0'
    else: st = '11' + st + '11'
    if int(st, 2) > 52:
        mas.append(int(st, 2))
print(min(mas))