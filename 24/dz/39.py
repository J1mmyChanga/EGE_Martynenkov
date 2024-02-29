s = open('files/24_2503.txt').readlines()
k = 0
for i in s:
    k_oao = k_aoa = 0
    for j in range(len(i)-2):
        if i[j] + i[j+1] + i[j+2] == 'OAO':
            k_oao += 1
        if i[j] + i[j+1] + i[j+2] == 'AOA':
            k_aoa += 1
    if k_aoa > k_oao:
        k += 1
print(k)