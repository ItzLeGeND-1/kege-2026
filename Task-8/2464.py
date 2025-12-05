from itertools import *
k=0
for pos,val in enumerate(product('НИЧЬЯ',repeat=7),start=1):
    val=''.join(val)
    if val.count('И') +val.count('Я')==2 and 'ИЯ' not in val and 'ЯИ' not in val and 'ИИ' not in val and 'ЯЯ' not in val:
        k+=1
print(k)
# for i in 'ИЯ'
#     val=val.replace(i, '*')
#  if val.count('*')==2 and '**' not in val:
#             k+=1