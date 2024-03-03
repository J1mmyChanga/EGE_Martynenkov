s = [int(x) for x in open('17_3579.txt')]
mas = []
minel = min(x for x in s if x % 6 == 0)
for i in range(len(s)-1):
    if s[i] % minel == 0 and s[i+1] % minel == 0:
        mas.append(s[i] + s[i+1])
print(len(mas), max(mas))