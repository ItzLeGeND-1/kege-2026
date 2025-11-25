from string import printable
def convert(num,sys):
    res=''
    while num!=0:
        res=printable[num%sys]+res
        num//=sys
    return res
num1=2*2187**2020+729**2021-2*243**2022+81**2023-2*27**2024-6561
d27=convert(num1,27)
#1 sposob
# K=0
# for i in range(10,27):
#     K+=d27.count(printable[i])
# print(K)
#2 sposob
# cnt_2=0
# for i in d27:
#     if int(i,27)>9:
#         cnt_2+=1
# print(cnt_2)
# 3 sposob
# cnt_1=0
# for i in d27:
#     if i in printable[10:27]:
#         cnt_1+=1
# print(cnt_1)
