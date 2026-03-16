def f(s,e,cnt=0):
    if s==e: return 1
    if s>e: return 0
    if s==24:
        cnt+=1
    if s==32:
        cnt+=1
    if cnt==2:
        return 0
    return f(s+1,e,cnt)+f(s+2,e,cnt)+f(s+4,e,cnt)+f(s+8,e,cnt)
print(f(16,24)*f(24,48)+f(16,32)*f(32,48))
