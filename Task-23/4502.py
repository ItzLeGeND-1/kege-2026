def f(start,end,cnt=0):
    cnt+=1
    if start==end and cnt==6: return 1
    if start>end: return 0
    return f(start+1,end,cnt)+f(start+2,end,cnt)+f(start*2,end,cnt)
for i in range(34,60):
    q=0
    q+=f(1,i)
    print(i,q)
print(q)
