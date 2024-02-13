mas = []
for n in range(1, 100):
    st = bin(n)[2:]
    if st.count('1') % 2 == 0: st = '10' + st[2:] + '0'
    else: st = '11' + st[2:] + '1'
    if int(st, 2) < 35:
        mas.append(n)
print(max(mas))