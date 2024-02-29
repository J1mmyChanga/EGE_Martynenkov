from string import ascii_uppercase

s = open('files/24_2507.txt').readlines()
m = 0
c = 0
k = 1
st = ''
let = ''
for i in s:
    for j in range(1, len(i)):
        if i[j] == i[j-1]:
            k += 1
        else:
            k = 1
        if k > m:
            m = k
            let = i[j]

print(m, let)

for i in s:
    if m*let in i:
        st = i
        break

d = {x:0 for x in ascii_uppercase}
for i in st.strip():
    d[i] += 1

for i in d:
    if d[i] == max(d.values()):
        maxis = i
        break

for i in s:
    c += i.count(maxis)
print(maxis, c)