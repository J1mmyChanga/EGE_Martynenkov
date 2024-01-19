from ipaddress import *
for n in range(33):
    net = ip_network(f'241.185.253.57/{n}', 0)
    if str(net).startswith('241.185.252.0'):
        print(net, net.netmask, n) #9