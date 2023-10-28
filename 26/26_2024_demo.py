def find_sp(num, sp):
    return sorted(list(filter(nu)))


with open('26_2024.txt') as f:
    data = sorted([(int(i.strip().split()[0]), int(i.strip().split()[1])) for i in f.readlines()[1:]], key=lambda x: x[0])
res = {}
for i in range(len(data)):
    sp = [data[i]]
    for j in data[i:-1]:
        if sp[-1][1] < data[i + 1][0]:
            sp += [j]
        else:
            continue
    if len(sp) > 1:
        res[tuple(sp)] = sp[-1][0] - sp[-2][1]
for i in sorted(list(res.items()), key=lambda x: x[0], reverse=True):
    print(i)