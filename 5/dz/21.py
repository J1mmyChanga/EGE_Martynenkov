mas = []
for n in range(2, 1000000):
    r = n
    if r % 3 == 0:
        r /= 3
    else:
        r -= 1
    if r % 5 == 0:
        r /= 5
    else:
        r -= 1
    if r % 11 == 0:
        r /= 11
    else:
        r -= 1
    if r == 8:
        mas.append(n)
print(len(mas))