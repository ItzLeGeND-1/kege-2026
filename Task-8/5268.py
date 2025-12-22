from itertools import permutations

k=0

for val in set(permutations('АМФИБРАХИЙ')):
    val=''.join(val)
    if 'ИИФАА' in val or 'ААФИИ' in val:
        k+=1
print(k)