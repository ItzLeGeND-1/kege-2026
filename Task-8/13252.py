from itertools import permutations
k=0
for val in set(permutations('КИДАЛА',r=5)):
    val=''.join(val)
    if 'КК' not in val and 'ИИ' not in val and 'ДД' not in val and 'АА' not in val and 'ЛЛ' not in val:
        k+=1
        print(val)
print(k)