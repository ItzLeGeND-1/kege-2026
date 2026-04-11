with open(r'.\files\26_589.txt') as file:
    N=int(file.readline())
    prices=[int(i) for i in file]
prices=sorted(prices)
groups=[]
summ_sale=0
max_sale=0
for i in range(0,max(prices),500):
    group=[j for j in prices if i<j<=i+500]
    sale_cnt=len(group)//2
    summ_sale+=sum(group[:sale_cnt])/2
    max_sale=max(max_sale,max(group[:sale_cnt]))
print(summ_sale,max_sale/2)


