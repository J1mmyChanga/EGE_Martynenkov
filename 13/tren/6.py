from ipaddress import *
for n in range(33):
    net = ip_network(f'76.155.48.2/{n}', 0)
    if str(net).startswith('76.155.48.0'):
        print(net.netmask) #