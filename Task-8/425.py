from itertools import permutations
k=0
for val in set(permutations('ЗАПИСЬ')):
    val=''.join(val)
    if val[0] not in 'Ь' and 'АЬ' not in val and 'ИЬ' not in val:
        k+=1
print(k)