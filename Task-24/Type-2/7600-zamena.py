from itertools import product
with open(r'..\files\24_7600.txt') as file:
    data=file.readline()
for val in product('QRS',repeat=2):
    val=''.join(val)
    data=data.replace(val,'* *')
data=data.split()
print(len(max(data,key=len)))
