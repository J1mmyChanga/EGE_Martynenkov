for n in range(1, 51):
    s = n * '6'
    while '66' in s:
        s = s.replace('66', '1', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('22', '6', 1)
    if s == '21':
        print(n)