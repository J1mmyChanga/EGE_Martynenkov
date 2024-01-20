from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [122, 21, 49, 91]))
print('.'.join(f'{x:>08b}' for x in [122, 21,48, 0])) #20

for n in range(33):
    net = ip_network(f'122.21.49.91/{n}', 0)
    if str(net).startswith('122.21.48.0'):
        print(net)