from itertools import product

a = []
for i in product('ЖИРАФ', repeat=5):
    s = ''.join(i)
    if s.count('Ж') == 1 and not s.startswith('Ф') and not s.endswith('Р'):
        a.append(s)
print(len(a))