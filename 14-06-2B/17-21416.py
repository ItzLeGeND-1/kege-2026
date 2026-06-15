with open(r'17_21416.txt') as file:
    data=[int(i)for i in file]
sum_otc=sum(i for i in data if i<0)
ans=[]
for num1,num2,num3 in zip(data,data[1:],data[2:]):
    nums=[num1,num2,num3]
    if min(nums)*max(nums)>sum_otc:
        ans.append(num1+num2+num3)
print(len(ans),max(ans))