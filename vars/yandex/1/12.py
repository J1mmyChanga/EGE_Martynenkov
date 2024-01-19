for n in range(10000, 4, -1):
    st = '5' + n * '2'
    while '52' in st or '2222' in st or '1112' in st:
        if '52' in st:
            st = st.replace('52', '11', 1)
            st = st.replace('2222', '5', 1)
        else:
            st = st.replace('1112', '2', 1)
    if sum(int(i) for i in st) == 1685:
        print(n)