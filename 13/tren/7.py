from ipaddress import *
# print('.'.join(f'{x:>08b}' for x in [112, 117, 107, 70]))
# print('.'.join(f'{x:>08b}' for x in [112, 117, 121, 80]))
# print(int('11100000', 2)) #224
for n in range(33):
    net1 = ip_network(f'112.117.107.70/{n}', 0)
    net2 = ip_network(f'112.117.121.80/{n}', 0)
    if net1 == net2:
        print(net1) #224