from itertools import permutations, product

a = []
for i in product('аоу', repeat=5):
    s = ''.join(i)
    a.append(s)
print(sorted(a).index('уауау') + 1)