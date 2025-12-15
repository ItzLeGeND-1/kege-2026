from itertools import product
k=0

for val in product('ДРАКОН',repeat=5):
    val=''.join(val)
    if val.count('Д')+val.count('Р')+val.count('А')>=1:
        k+=1
for val in product('КОНЕЦ',repeat=5):
    val=''.join(val)
    if val.count('Е')+val.count('Ц'):
        k+=1
print(k)