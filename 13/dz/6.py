from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [158, 116, 11, 146]))
print('.'.join(f'{x:>08b}' for x in [158, 116, 0, 0])) #7

for n in range(33):
    net = ip_network(f'158.116.11.146/{n}', 0)
    if str(net).startswith('158.116.0.0'):
        print(net)