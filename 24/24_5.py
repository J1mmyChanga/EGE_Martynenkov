with open('24-5.txt') as f:
    data = f.read()
max_k = 0
k = 0
for i in data:
    if i == ')':
        k += 1
    else:
        if k > max_k:
            max_k = k
        k = 0
print(max_k)