a = input().split(';')
b = input()
mn_b = set(b)
new = []
for el in a:
    if int(el) % int(b) == 0:
        for cif in el:
            if cif in mn_b:
                break
        else:
            new.append(int(el))
print(max(new))