a = input().split(';')
b = set(input())

for el in a:
    if int(el) % int(b) == 0:
        for cif in el:
            if cif in a:
                break
        else:
            new.append(int(el))
print(max(new))