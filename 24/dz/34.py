s = open('files/24_2500.txt').readline()
k = 0
for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    k += s.count(f'G{i}ME')
print(k)