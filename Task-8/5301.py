from itertools import product
k=0
for val in product('ЛЕСЯ ',repeat=5):
    val=''.join(val)
    if val[0]!=' ' and val[-1]!=' ':
        val=val.replace('Л','*')
        val = val.replace('С', '*')
        val = val.replace('Е', '!')
        val = val.replace('Я', '!')
        if '**' not in val and "!!" not in val and val.count(' ')==1:
            print(val)
            k+=1
print(k)