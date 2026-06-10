with open(r'../../files/26_6641.txt') as file:
    N,M=map(int,file.readline().split())

    prices=[list(map(int,i.replace('S','1').replace('W','0').split()))for i in file]
prices=sorted(prices,key=lambda x:(x[0],-x[1]))



cnt_S=0
bought=[]
summ=0
for cost in prices:
    if summ+cost[0]<=M:
        summ+=cost[0]
        bought.append(cost)
        cnt_S+=cost[1]


pos_bought=len(bought)

for cost_1 in bought[::-1]:
    if cost_1[1]==0:
        for cost_2 in prices[pos_bought:]:
            pos_bought += 1
            if cost_2[1]==1:
                if summ - cost_1[0] + cost_2[0] <=M:
                    bought.remove(cost_1)
                    bought.append(cost_2)
                    cnt_S+=1
                    summ=summ-cost_1[0]+cost_2[0]
                    break
print(cnt_S,M-summ)




