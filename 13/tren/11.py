from ipaddress import *

# print('.'.join(f'{x:>08b}' for x in [175, 122, 80, 13]))
# print('.'.join(f'{x:>08b}' for x in [175, 122, 80, 0])) #7
for n in range(33):
    net = ip_network(f'175.122.80.13/{n}', 0)
    if net.num_addresses >= 60 and str(net).startswith('175.122.80.0'):
        print(net.netmask)