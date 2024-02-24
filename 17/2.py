a = [int(x) for x in open('files/17_2013.txt')]
ans = []

for i in a:
    if (i%10==2 or i%10==7) and i % 3 == 0 and i % 11 == 0:
        ans.append(i)

print(len(ans), min(ans))