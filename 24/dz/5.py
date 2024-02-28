s = open('files/24_1975.txt').readline()
for n in range(2, 10000):
    s = s.replace('P'*n, 'P P')
print(max(len(c) for c in s.split()))