from ipaddress import *

k = 0
net = ip_network('212.192.32.96/255.255.255.224')
for i in net:
    if '000' not in f'{i:b}'[24:] and '111' not in f'{i:b}'[24:]:
        k+=1
        print(f'{i:b}')
print(k)