from itertools import *
k=0
# product - функция, которая формирует все возможные комбинации символов длиной repeat
for i in product('екмопрть',repeat=5):
    s=''.join(i)
    k+=1
    if s[0] not in 'ь' and s.count('к')==2:
        print(s,k)

#permutations - функция, которая формирует все возможные перестановки символов
alph='ПРИВЕТ'
# enumerate - нумерует элементы последовательности  от start
res=enumerate(alph,start=1)
print(*res)