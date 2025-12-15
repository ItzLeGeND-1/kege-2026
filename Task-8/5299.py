from itertools import permutations
k=0
for val in set(permutations('ХОЧУ СОТКУ',)):
    val=''.join(val)
    if ' ' not in val[0] and ' ' not in val[-1] and 'У' not in val[0] and ' У' not in val:
        k+=1
        print(val)
print(k)