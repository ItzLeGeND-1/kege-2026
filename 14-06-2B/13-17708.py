from ipaddress import *

def f(ip):
    ip=f'{int(ip):032b}'
    return ip.count('1')%4==0 and ip[-2:]=='11'
net=ip_network('211.46.0.0/255.255.128.0',False)

k=0
for ip in net:
    if f(ip):
        k+=1
print(k)