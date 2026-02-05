from string import printable
s=2 * 729**2014 +2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024
k=0
res=''
while s!=0:
    res=printable[s%27]+res
    s//=27
for i in res:
    if i<='9':
        k+=1
print(len(res)-k)