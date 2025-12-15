from itertools import permutations
k=0
for val in set(permutations('ВОРОТА',r=6)):
    val=''.join(val)
    if 'ОО' not in val and 'ОА' not in val and 'АО' not in val:
        k+=1
print(k)
