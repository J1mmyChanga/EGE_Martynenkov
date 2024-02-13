for n in range(1, 1000):
    st = bin(2 * n)[2:]
    st += str(st.count('1') % 2)
    st += str(st.count('1') % 2)
    if int(st, 2) > 1017:
        print(n)