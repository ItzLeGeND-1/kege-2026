ten=4*625**9 - 25**15 + 2*5**11 - 7
res=''
while ten!=0:
    res=str(ten%5)+res
    ten//=5
print(res.count('4'))


##############################################
ten=4*625**9 - 25**15 + 2*5**11 - 7


cnt4=0
while ten:
    if ten%5==4:
        cnt4+=1
    ten//=5
print(cnt4)



