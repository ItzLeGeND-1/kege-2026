with open(r'../../files/26_23208.txt') as file:
    N=int(file.readline())
    details=[]
    for num,line in enumerate(file,start=1):
        grind,paint=map(int,line.split())
        details.append([grind,'G',num])
        details.append([paint, 'S', num])

details=sorted(details)

converyor=[0]*N
last_id=0
cnt_grind=0
for detail in details:
    if detail[2] not in converyor:
        if detail[1]=='G':
            converyor[converyor.index(0)]= detail[2]
            cnt_grind+=1
        else:
            converyor[-converyor[::-1].index(0)-1]=detail[2]
        last_id=detail
print(last_id[2],cnt_grind-1 if last_id[1]=='G' else cnt_grind )

##############################################################################

with open(r'../../files/26_23208.txt') as file:
    N=int(file.readline())
    details=[]
    for num,line in enumerate(file,start=1):
        time_1,time_2=map(int,line.split())
        if min(time_1,time_2)==time_1:
            details.append([time_1,'G',num])
        else:
            details.append([time_2,'O',num])
details=sorted(details)
cnt_grind=sum(d[1]=='G'for d in details[:-1])
print(details[-1][2],cnt_grind)
