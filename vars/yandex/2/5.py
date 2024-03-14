for n in range(1000, 10000):
    if len(str(n)) != len(set(str(n))):
        continue
    s = sorted([int(x) for x in str(n)])
    r = f'{min(s[0]+s[3], s[1]*s[2])}{max(s[0]+s[3], s[1]*s[2])}'
    if int(r) > 85:
        print(n, r)