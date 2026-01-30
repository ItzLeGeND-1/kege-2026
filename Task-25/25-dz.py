from fnmatch import fnmatch
k=0
q=0
for n in range(128064-128064%596,10**12+1,596):
    if fnmatch(str(n),'1*28?64') and n%596==0:
       k+=1
       q+=n
print(k,q/k)