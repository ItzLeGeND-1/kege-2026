from ipaddress import *

net=ip_network('172.16.192.0/255.255.192.0')

cnt=0
for ip in net:
    ip=str(ip)
    ip=ip.replace('.','')
    ip=f'{int(ip):032b}'
    if ip.count('1')%5!=0 and len(ip)==32 and ip.count('1')!=32 and ip.count('0')!=32:
        print(ip)
        cnt+=1
print(*net)
print(cnt)