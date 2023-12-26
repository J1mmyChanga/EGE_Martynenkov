d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 1, 'e': 2, 'f': 3}
d1 = {**d, **d2}
sp = [1, 2, 3, 4, 5, 6, 7]
a, *b, c = sp
print(a, b, c)
print(*d1)
print(list(range(*[1, 3])))