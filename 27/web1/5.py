from math import factorial

f = open('files/27B_2723.txt')
n = int(f.readline())
k = k19 = 0
for i in range(n):
    x = int(f.readline())
    if x % 19 == 0: k19 += 1
    else: k += 1
print(factorial(k19)//(factorial(3)*factorial(k19 - 3)))