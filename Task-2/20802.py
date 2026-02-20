from itertools import product,permutations
def f(w,x,y,z):
    return (w <=(not(z<=x)))or y
for a,b,c,d,e,g,k in product([0,1],repeat=7):
    tab=[(1,a,b,c),
         (0,1,0,d),
         (e,0,g,k)
    ]
    if len(tab)==len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t)))for t in tab]==[0,0,0]:
                print(*p)