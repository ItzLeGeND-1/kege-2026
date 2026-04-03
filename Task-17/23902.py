with open(r'.\files\17_23902.txt') as file:
    data=[int(i)for i in file]
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1= str(num1)[0]==str(num1)[-1]
    u2 = str(num2)[0] == str(num2)[-1]
    u3 = str(num3)[0] == str(num3)[-1]
    u4 = 1000<=num1<=9999 and str(num1)[1]=='2'
    u5 = 1000 <= num2 <= 9999 and str(num2)[1]=='2'
    u6 = 1000 <= num3 <= 9999 and str(num3)[1]=='2'
    if u1+u2+u3==1 and u4+u5+u6==2:
        ans.append(max(num1,num2,num3))
print(len(ans),sum(ans))