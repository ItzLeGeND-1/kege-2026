with open(r'.\files\17_3749.txt') as file:
    data=[int(i)for i in file]
maxx=max(i for i in data if i**.5==int(i**0.5))*3
print(maxx)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1= num1<=maxx
    u2 = num2 <= maxx
    if  u1+u2>=1 and (num1*num2)**0.5==int((num1*num2)**0.5):
        ans.append((num1*num2)**0.5)
print(len(ans),int(max(ans)+min(ans)))