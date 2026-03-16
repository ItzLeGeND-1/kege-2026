def f(a,s,m):
    if a+s>=100: return m%2==0
    if m==0: return 0
    h=[f(a+3,s,m-1),f(a*2,s,m-1),f(a,s+3,m-1),f(a,s*2,m-1)]
    return any(h) if m%2!=0 else all(h)
print('19.',[s for s in range(1,83) if( not f(17,s,1) and f(17,s,2))])
print('20.',[s for s in range(1,83) if(not f(17,s,1) and f(17,s,3))])
print()