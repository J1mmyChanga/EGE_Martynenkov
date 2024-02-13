for n in range(1, 140):
    st = bin(n)[2:]
    st += str(st.count('1') % 2)
    st += str(st.count('1') % 2)
    print(n, int(st, 2))