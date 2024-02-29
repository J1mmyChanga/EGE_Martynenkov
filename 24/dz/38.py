s = open('files/24_2502.txt').readlines()
k = 0
for i in s:
    for j in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        if i.count(f'K{j}GE') >= 1:
            k += 1
            break
print(k)