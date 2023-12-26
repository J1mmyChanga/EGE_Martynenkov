from itertools import permutations, product

a = []
for i in product('АКРУ', repeat=5):
    s = ''.join(i)
    a.append(s)
for i in sorted(a):
    print(sorted(a)[149])