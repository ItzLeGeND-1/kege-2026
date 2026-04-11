with open(r'.\files\26_23383.txt') as file:
    N=int(file.readline())
    check_points={}
    for i in file:
        sportsmen,point= map(int,i.split())
        if point not in check_points:
            check_points[point]={sportsmen}
        else:
            check_points[point].add(sportsmen)

ans=[]
for point in check_points:
    cnt=1
    max_cnt=0
    sort_sportsmen=sorted(check_points[point])
    for sp1,sp2 in zip(sort_sportsmen,sort_sportsmen[1:]):
        if sp2-sp1==1:
            cnt+=1
        else:
            max_cnt=max(max_cnt,cnt)
            cnt=1
    max_cnt=max(max_cnt,cnt)
    ans.append([max_cnt,point])
print(sorted(ans,key=lambda x:(-x[0],x[1]))[0])
