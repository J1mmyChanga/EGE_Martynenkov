from ipaddress import *

# print('.'.join(f'{x:>08b}' for x in [211, 48, 136, 64]))
# print('.'.join(f'{x:>08b}' for x in [255, 255, 255, 224])) #8

c = 0
net = ip_network('211.48.136.64/255.255.255.224')
for i in net:
    if f'{i:b}'.endswith('11'):
        c += 1
print(c)