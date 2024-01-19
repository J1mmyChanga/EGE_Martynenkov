from ipaddress import *

#print('.'.join(f'{x:>08b}' for x in [255, 255, 254, 0]))
# print(2 ** 9 - 2) #510

net = ip_network('135.12.171.214/255.255.254.0', False)
print(net.num_addresses - 2)