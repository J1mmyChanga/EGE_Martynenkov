from ipaddress import *
print('.'.join(f'{x:>08b}' for x in [165, 112, 200, 70]))
print('.'.join(f'{x:>08b}' for x in [165, 112, 175, 80])) # 17

for n in range(33):
    net1 = ip_network(f'165.112.200.70/{n}', 0)
    net2 = ip_network(f'165.112.175.80/{n}', 0)
    if net1 == net2:
        print(net1)