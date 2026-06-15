from itertools import product,permutations
def f(x,y,z,w):
    return (not(x==w and (not z)))and(y==x and (not w))
for a,b,c,d,e,g in product([0,1],repeat=6):
    tab=[(a,b,0,c),
         (d,0,e,0),
         (0,g,1,0)]
    if len(tab)==len(set(tab)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p,t)))for t in tab]==[1,1,1]:
                print(*p)
