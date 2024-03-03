def f(a, b, m):
    if a + b >= 223:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [
        f(a+1, b, m-1), f(a*2, b, m-1),
        f(a, b+1, m-1), f(a, b*2, m-1),
    ]
    return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(1, 206) if f(17, s, 2)])
print('20)', [s for s in range(1, 206) if not f(17, s, 1) and f(17, s, 3)])
print('19)', [s for s in range(1, 206) if f(17, s, 4) and not f(17, s, 2)])