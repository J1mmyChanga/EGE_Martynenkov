from ipaddress import *
# print('.'.join(f'{x:>08b}' for x in [111, 81, 208, 27]))
# print('.'.join(f'{x:>08b}' for x in [111, 81, 192, 0]))
# print(int('11000000', 2)) #192

for n in range(33):
    net = ip_network(f'111.81.208.27/{n}', 0)
    if str(net).startswith('111.81.192.0'):
        print(n, net.netmask)
print(int('11000000', 2)) #192