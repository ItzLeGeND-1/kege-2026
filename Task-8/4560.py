from itertools import permutations
k=0
for val in permutations('ТИХОРЕЦК',r=4):
    val=''.join(val)
    komar=0
    if val.count('И')+val.count('О')+val.count('Е')==2:
        if val[0]=='Т':
            komar+=1
        if val[1]=='И':
            komar+=1
        if val[2]=='Х':
            komar+=1
        if val[3]=='О':
            komar+=1
        if komar==2:
            k+=1
        print(val)
print(k)