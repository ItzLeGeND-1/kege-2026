from itertools import product, permutations

def f(x,y,z,w):
    return not(y<=x)or(z<=w)or not z


for a, b, c, d, e, g, h in product((0, 1), repeat=7):
    table = [
        (a, 0, b, c),
        (0, 1, d, e),
        (1, g, h, 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,t))) for t in table]==[0,0,0]:
                print(*p, sep='')
