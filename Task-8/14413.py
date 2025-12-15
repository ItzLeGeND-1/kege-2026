from itertools import permutations

k=0

for val in set(permutations('СОРТИРОВКА')):
    val=''.join(val)
    for i in 'СРТВК':
        val = val.replace(i, '*')
    for i in 'ОИА':
        val = val.replace(i, '!')
    if '***' not in val and '!!!' not in val:
        k+=1
print(k)
