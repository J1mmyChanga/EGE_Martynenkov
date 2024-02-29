s = open('files/24_587.txt').readlines()
k = 0
for i in s:
    if i.count('B') / i.count('A') >= 1.05:
        k += 1
print(k)