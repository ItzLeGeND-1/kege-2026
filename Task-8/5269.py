from itertools import permutations
k=0
for val in set(permutations('АМФИБРАХИЙ')):
    val=''.join(val)
    if val[len(val)//2-1:len(val)//2+1]=='БР':
        k+=1
        print(val)
print(k)