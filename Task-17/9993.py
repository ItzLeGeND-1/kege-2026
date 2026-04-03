with open(r'.\files\17_9993.txt') as file:
    data=[int(i)for i in file]
def is_prime(num):
    if num<2: return False
    for i in range(2,int(num**.5)+1):
        if num%i==0:
            return False
    return True
max_17=max(i for i in data if abs(i)%100==17)
ans=[]
for num1,num2 in zip(data,data[1:]):
    u1 = is_prime(num1)
    u2 = is_prime(num2)
    summ=num1+num2
    if summ%max_17==0 and u1+u2==1:
        ans.append(num1*num2)
print(len(ans),max(ans))