with open(r'.\files\17_17636.txt') as file:
    data=[int(i)for i in file]
max_3=max(i for i in data if abs(i)%10==3 and 100<=i<=999)
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1= 100<=abs(num1)<=999 and abs(num1)%10==3
    u2 = 100 <= abs(num2) <= 999 and abs(num2) % 10 == 3
    u3 = 100 <= abs(num3) <= 999 and abs(num3) % 10 == 3
    if u1+u2+u3>=1 and num1+num2+num3<max_3:
        ans.append(num1+num2+num3)
print(len(ans),max(ans))
