d=set()
def f(start,cnt):
    if cnt==8:
        if 1000<=start<=1024:
            d.add(start)
    else:
        f(start+1,cnt+1)
        f(start + 5, cnt + 1)
        f(start * 3, cnt + 1)
f(1,0)
print(len(d))
