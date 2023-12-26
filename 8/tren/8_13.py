from itertools import permutations

a = []
for i in permutations('КАЛИЙ'):
    s = ''.join(i)
    if 'ИА' not in s and not s.startswith('Й'):
        a.append(s)
print(len(a))