from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [173, 103, 25, 118]))
print('.'.join(f'{x:>08b}' for x in [173, 103, 24, 0])) # 11

for n in range(33):
    net = ip_network(f'173.103.25.118/{n}', 0)
    if str(net).startswith('173.103.24.0'):
        print(net)