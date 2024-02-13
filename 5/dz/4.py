for n in range(1, 100):
    st = bin(n)[2:]
    st += st[-1]
    if st.count('1') % 2 == 0: st += '0'
    else: st += '1'
    if st.count('1') % 2 == 0: st += '0'
    else: st += '1'
    print(n, int(st, 2))