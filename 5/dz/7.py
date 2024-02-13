mas = []
for n in range(1, 100):
    st = bin(n)[2:]
    st += str(st.count('1') % 2)
    st += str(st.count('1') % 2)
    if int(st, 2) < 80:
        mas.append(int(st, 2))
    print(n, int(st, 2))
print(len(mas))