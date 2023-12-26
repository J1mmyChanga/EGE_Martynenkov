from itertools import permutations

a = []
for i in permutations('ПЕСКАРЬ'):
    s = ''.join(i)
    if s[0] != 'Ь' and 'ЬЕ' not in s and 'ЬА' not in s and 'ЬР' not in s:
        a.append(s)
print(len(a))