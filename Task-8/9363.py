from itertools import permutations
k=0
for val in permutations('ХОЧУНАБЮДЖЕТ'):
    val=''.join(val)
    for i in 'ОУАЮЕ':
        val=val.replace(i,'*')
    if "*****" not in val:
        k+=1
print(k)