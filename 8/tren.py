from itertools import permutations, product


a = []
for i in product('ТИМАШЕВСК', repeat=6):
    s = ''.join(i)
    count_gl = s.count('И') + s.count('А') + s.count('Е')
    count_sogl = 6 - count_gl
    s = s.replace('М', 'Т').replace('В', 'Т').replace('С', 'Т').replace('К', 'Т')\
    .replace('А', 'И').replace('Е', 'И')
    if 'ШТ' not in s and 'ТШ' not in s and 'ШШ' not in s and count_gl < count_sogl:
        a.append(s)
print(len(a))