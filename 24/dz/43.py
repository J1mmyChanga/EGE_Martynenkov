from string import ascii_uppercase

s = open('files/24_2509.txt').readline()
d = {x:0 for x in ascii_uppercase}
for i in s.strip():
    d[i] += 1
print(max(d.values()) - min(d.values()))