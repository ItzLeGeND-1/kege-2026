from ipaddress import *

ip_1=ip_address('153.202.16.37')
ip_hosts=ip_address('153.202.16.32')
cnt=0
for mask in range(16,33):
    net=ip_network(f'218.48.192.56/{mask}',False)
    if ip_hosts in net.hosts() and ip_1 == net.network_address:
        print(mask)