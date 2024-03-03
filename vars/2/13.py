from ipaddress import *

print('.'.join(f'{x:>08b}' for x in [156, 133, 216, 35]))
print('.'.join(f'{x:>08b}' for x in [156, 133, 216, 0]))

for i in range(33):
    net = ip_network(f'156.133.216.35/{i}', 0)
    if str(net.network_address) == '156.133.216.0':
        print(net.num_addresses)
print(2**11)