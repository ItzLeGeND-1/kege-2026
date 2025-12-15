from itertools import permutations

k=0

for val in set(permutations('ПАРИЖАНКА')):
    val=''.join(val)
    if val.count('АИ')+val.count('АА')+val.count('ИА')==1 and 'ААА' not in val:
        k+=1
        print(val)
print(k)