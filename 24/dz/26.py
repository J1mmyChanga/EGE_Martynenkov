s = open('files/24_2425.txt').readline()
for i in range(1, 1000):
    if i*'DBAC' not in s:
        print(i - 1)
        break
print(23*'DBAC'+'DBA' in s)
print(23*4+3)