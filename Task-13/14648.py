from ipaddress import *
from ipaddress import ip_address

ip_1=ip_address('218.48.192.0')
ip_hosts=ip_address('218.48.192.56')
cnt=0
for mask in range(16,25):
    net=ip_network(f'218.48.192.56/{mask}',False)
    if ip_hosts in net.hosts() and ip_1 == net.network_address:
        if  net.num_addresses-2>=500:
         cnt+=1
print(cnt)