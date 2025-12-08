from itertools import *
k=0
for pos,val in enumerate(product('ДИОНСЙ',repeat=6),start=1):
    val=''.join(val)
    if ((val.count('Д')>=1 and val.count('Н')==0) or (val.count('Д')==0 and val.count('Н')>=1)) and 'ДД' not in val and 'ИИ' not in val and 'ОО' not in val and 'НН' not in val and 'НН' not in val and 'СС' not in val and 'ЙЙ' not in val:
        k+=1
print(k)