from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [10, 8, 248, 131]))
print('.'.join(f'{x:>08b}' for x in [255, 255, 224, 0]))
print(int('11100000', 2))

net = ip_network(f'10.8.248.131/255.255.224.0', 0)
print(net)