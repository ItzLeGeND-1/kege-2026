from itertools import product,permutations

def f(x,y,z,w):
    return w<=((x<=z)<=y)
for a,b,c,d,e,g,h in product([0,1],repeat=7):
    tab=[(a,b,0,1),
         (c,0,1,d),
         (e,g,h,0)]
    if len(tab)==len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t)))for t in tab]==[0,0,0]:
                print(*p)