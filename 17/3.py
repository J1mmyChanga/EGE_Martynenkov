a = [int(x) for x in open('files/17_2015.txt')]
ans = []

for i in a:
    if (i % 10 == 5 or i % 10 == 7) and i % 9 != 0 and i % 11 != 0:
        ans.append(i)

print(len(ans), max(ans) + min(ans))