from ipaddress import *
for n in range(33):
    net = ip_network(f'148.195.140.28/{n}', 0)
    if str(net).startswith('148.195.140.0'):
        print(net, net.netmask, n)
        break #22