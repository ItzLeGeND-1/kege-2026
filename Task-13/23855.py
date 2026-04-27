from ipaddress import *

net=ip_network('172.95.116.174/255.255.192.0',False)
ans=[*net.hosts()]
print(min(ans),172+95+64+1)