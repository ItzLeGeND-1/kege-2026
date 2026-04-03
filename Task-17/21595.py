with open(r'.\files\17_21595.txt') as file:
    data=[int(i)for i in file]
max_len=len([i for i in data if 1000<=abs(i)<=9999 and abs(i)%10==3])**2
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    sp=sorted([num1,num2,num3])
    u1=sp[1]+sp[2]>max_len
    if u1:
        ans.append(num1+num2+num3)
print(len(ans),max(ans))


