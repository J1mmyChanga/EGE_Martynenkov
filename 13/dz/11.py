from ipaddress import *
net = ip_network(f'192.168.240.0/255.255.255.0')
c = 0
for i in net:
    if f'{i:b}'.count('1') == 16:
        c += 1
print(c)