mas = []
for n in range(1, 100):
    res = ''
    st = bin(n)[2:][::-1]
    if n <= 100 and int(st, 2) == 13:
        mas.append(n)
print(mas, max(mas))