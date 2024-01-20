from ipaddress import *

print('.'.join(f'{x:>08b}' for x in [154, 201, 208, 17]))
print('.'.join(f'{x:>08b}' for x in [154, 201, 192, 0]))
print(int('11100000', 2))

for n in range(33):
    net = ip_network(f'154.201.208.17/{n}', 0)
    if str(net).startswith('154.201.192.0'):
        print(n)