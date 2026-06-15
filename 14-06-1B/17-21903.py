with open(r'17_21903.txt') as file:
    data=[int(i)for i in file]

min_13=min(i for i in data if abs(i)%100==15 and 99<abs(i)<1000)
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    u1= num1>0
    u2 = num2 > 0
    u3 = num3 > 0
    nums=[num1,num2,num3]
    if (u1+u2+u3==0 or u1+u2+u3==3)and min(nums)*max(nums)>min_13**2:
        ans.append(min(nums)*max(nums))
print(len(ans),min(ans))