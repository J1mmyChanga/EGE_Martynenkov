from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [10, 96, 180, 231]))
print('.'.join(f'{x:>08b}' for x in [10, 96, 140, 118])) #13

for n in range(33):
    net1 = ip_network(f'10.96.180.231/{n}', 0)
    net2 = ip_network(f'10.96.140.128/{n}', 0)
    if net1 != net2:
        print(f'{net1.netmask:b}')