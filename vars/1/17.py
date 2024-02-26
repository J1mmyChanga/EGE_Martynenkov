a = [int(x) for x in open('17-385.txt')]
sp = [sum(int(x) for x in str(num)) for num in a]
num = min(sp)
mas = [x for x in a if sum(int(i) for i in str(x)) == num]
main_num = max(mas)

sums = []
res = []
for i in range(len(a) - 1):
    if a[i] > main_num and a[i+1] > main_num:
        sums.append(a[i] + a[i+1])
        res.append(sum(int(i) for i in str(a[i])) + sum(int(i) for i in str(a[i+1])))
print(len(sums), max(res))