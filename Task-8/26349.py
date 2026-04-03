from itertools import product
print(sorted('СУЛАК'))
alph=sorted('СУЛАК')
cnt=0
for val in product(alph,repeat=6):
    val=''.join(val)
    cnt+=1
print(cnt)