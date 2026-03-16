def f(x,s):
    if x<=13: return s%2==0
    if s==0: return None
    h=[f(x-2,s-1),f(x//1.5,s-1)]
    return any(h) if (s-1)%2==0 else all(h)
print('19',[x for x in range(14,1000) if f(x,2)])
print('20',[x for x in range(14,1000) if not f(x,1) and f(x,3)])
print('21',[x for x in range(14,1000) if not f(x,2) and f(x,4)])