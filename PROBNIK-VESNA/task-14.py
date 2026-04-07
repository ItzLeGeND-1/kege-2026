ans=[]
for x in range(1,9431):
    s=39**483+39**235-x
    cnt=0
    while s!=0:
        if s%37==0: cnt+=1
        s//=37
    ans.append(cnt)
print(max(ans))

