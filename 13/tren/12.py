from ipaddress import *

# print('.'.join(f'{x:>08b}' for x in [184, 178, 54, 144]))
# print('.'.join(f'{x:>08b}' for x in [255, 255, 255, 240]))

c = 0
net = ip_network('184.178.54.144/255.255.255.240')
for i in net:
    if '111' in f'{i:b}':
        c += 1
print(c)