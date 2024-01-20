from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [191, 173, 145, 240]))
print('.'.join(f'{x:>08b}' for x in [191, 173, 144, 0])) #512

for n in range(33):
    net = ip_network(f'191.173.145.240/{n}', 0)
    if str(net).startswith('191.173.144.0'):
        print(net, f'{net.netmask:b}')