from itertools import permutations, product

a = []
for i in product('МАНГУСТ', repeat=6):
    s = ''.join(i)
    a.append(s)
a = sorted(a)
for i in range(len(a)):
    if a[i][0] != 'У' and a[i].count('М') == 2 and a[i].count('Г') <= 1:
        print(i + 1)