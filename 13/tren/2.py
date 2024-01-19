from ipaddress import *
# print('.'.join(f'{x:>08b}' for x in [220, 128, 96, 0]))
# print('.'.join(f'{x:>08b}' for x in [220, 128, 112, 142]))
# print(int('11100000', 2)) #224

for n in range(1, 33):
    net = ip_network(f'220.128.112.142/{n}', 0)
    if str(net).startswith('220.128.96.0'):
        print(n)
print(int('11100000', 2)) #224
