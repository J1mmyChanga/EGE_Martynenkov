s = open('files/24_859.txt').readlines()
k = 0
for i in s:
    if i.count('S') == i.count('X'):
        k += 1
print(k)