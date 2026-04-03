with open(r'.\files\17_17558.txt') as file:
    data=[int(i)for i in file]
k=0
for i in data:
    if i%32==0:
        k+=1
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1= num1<0
    u2 = num2 < 0
    summ=num1+num2
    if summ<=k and u1+u2>=1:
        ans.append(summ)
print(len(ans),max(ans))