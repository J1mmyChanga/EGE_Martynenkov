a = [int(x) for x in open('files/17_2309.txt')]
ans_11 = []
ans_17 = []
for i in a:
    if i % 11 == 0:
        ans_11.append(i)
    if i % 17 == 0:
        ans_17.append(i)
if len(ans_11) > len(ans_17):
    print(len(ans_11), min(ans_11))
else:
    print(len(ans_17), max(ans_17))
