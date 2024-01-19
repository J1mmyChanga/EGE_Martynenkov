from ipaddress import *
# print('.'.join(f'{x:>08b}' for x in [108, 133, 75, 91]))
# print('.'.join(f'{x:>08b}' for x in [108, 133, 75, 64])) #64
for n in range(33):
    net = ip_network(f'108.133.75.91/{n}', 0)
    if str(net).startswith('108.133.75.64'):
        print(net, net.num_addresses)