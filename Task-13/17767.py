from ipaddress import *

net=ip_network('228.172.236.0/20')
cnt=0
for ip in net:
    ip=f'{int(ip):032b}'
    if ip.count('1')%5!=0:
        cnt+=1
print(cnt)