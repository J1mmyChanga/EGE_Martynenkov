from ipaddress import *

# print('.'.join(f'{x:>08b}' for x in [192, 168, 156, 235]))
# print('.'.join(f'{x:>08b}' for x in [255, 255, 255, 240])) #11
# print(int('1011', 2))

net = ip_network('192.168.156.235/255.255.255.240', 0) #192.168.156.224
ip1 = ip_address('192.168.156.235')
ip2 = ip_address('192.168.156.224')
print(int(ip1) - int(ip2))