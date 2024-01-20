from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [118, 193, 30, 139]))
print('.'.join(f'{x:>08b}' for x in [118, 193, 24, 0]))
print(int('11111000', 2))

for n in range(33):
    net = ip_network(f'118.193.30.139/{n}', 0)
    if str(net).startswith('118.193.24.0'):
        print(n)