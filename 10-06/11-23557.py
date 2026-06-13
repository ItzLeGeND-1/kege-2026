from math import *

for L in range(1,10**10):
    N=52+500+10
    i=ceil(log2(N))
    I=ceil(i/8*L)
    if I*45_877>49*2**20:
        print(L)
        break