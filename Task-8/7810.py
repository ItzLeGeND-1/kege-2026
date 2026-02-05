from itertools import product
k=0
for val in product('М*СЛ*',repeat=6):
    if val.count('*')==1:
        k+=1
print(k)