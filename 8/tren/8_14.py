from itertools import permutations

a = []
for i in permutations('КОЛУН'):
    s = ''.join(i)
    if s[1] in 'ОУ' and s[3] in 'ОУ':
        a.append(s)
print(len(a))