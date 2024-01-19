from ipaddress import *
ip_add = '.'.join(f'{x:>08b}' for x in [135, 12, 171, 214])
mask = '.'.join(f'{x:>08b}' for x in [255, 255, 248, 0])
print(ip_add)
print(mask)
# print(int('10101000', 2)) #135.12.168.0
net = ip_network('135.12.171.214/255.255.248.0', False)
print(net)