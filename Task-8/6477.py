from itertools import permutations
k=0
for val in set(permutations('ЛЕВИОСА')):
    val=''.join(val)
    if  val[0] not in 'ЕИОА' and val[3] not in 'ЛВС':
        k+=1
print(k)

