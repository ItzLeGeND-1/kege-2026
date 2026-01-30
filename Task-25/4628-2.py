from string import printable
from itertools import product
ans=[]
for V in printable[:10]:
   for l in range(0,3):
    for val in product('0123456789',repeat=l):
        val= '12' + ''.join(val)+ '4'+ V + '65'
        if int(val)%161==0:
            ans.append([val,int(val)//161])
for i in sorted(ans):
    print(*i)