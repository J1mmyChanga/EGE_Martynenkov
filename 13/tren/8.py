from ipaddress import *
# print('.'.join(f'{x:>08b}' for x in [157, 127, 182, 76]))
# print('.'.join(f'{x:>08b}' for x in [157, 127, 190, 80])) #21
for n in range(33):
    net1 = ip_network(f'157.127.182.76/{n}', 0)
    net2 = ip_network(f'157.127.190.80/{n}', 0)
    if net1 != net2:
        print(net1, net2) #21