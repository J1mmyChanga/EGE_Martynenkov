from itertools import permutations, product

a = []
for i in product('КОМПЬЮТЕР', repeat=5):
    s = ''.join(i)
    a.append(s)
a = sorted(a)
k = 0
for i in range(len(a)):
    if (i + 1) % 2 != 0 and a[i][0] != 'Ь' and a[i].count('К') == 2:
        k += 1
print(k)