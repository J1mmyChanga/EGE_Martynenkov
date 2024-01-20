from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [255, 255, 240, 0])) # 2 ** 12 - 2 = 4094

net = ip_network(f'0.0.0.0/255.255.240.0', 0)
print(net.num_addresses - 2)