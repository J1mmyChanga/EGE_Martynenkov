from ipaddress import *
c = 0
net = ip_network('10.48.96.0/255.255.240.0')
for i in net:
    if f'{i:b}'.count('1') > f'{i:b}'.count('0'):
        c += 1
print(c)