
Задание 25(маски)
# Задачи с масками

# Библиотека для проверки строк под маску
from fnmatch import fnmatch

# ? - ровно один любой символ
# * - любое кол-во любых символов

print(fnmatch('', '*'))


# КомпЕГЭ 4603 (рекомендованное решение)
from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
   if fnmatch(str(N), '1234*7'):
       print(N, N // 141)

#########################################
print('#################')

# КомпЕГЭ 4603 (решение перебором)
from itertools import product

for l in range(0, 4):
    for val in product('0123456789', repeat=l):
        val = '1234' + ''.join(val) + '7'
        if int(val) % 141 == 0:
            print(val, int(val) // 141)
# ПОИСК МНОЖИТЕЛЕЙ ЧИСЛА
            # ЛУЧШИЙ СПОСОБ
def fact_3(num):
            d = []
            while num % 2 == 0:
                    d += [2]
                    num //=2
            i = 3
            while i * i <= num:
                    while num % i == 0:
                        d += [i]
                        num //= i
                    i += 2
            if num > 2:
                    d += [num]
            return d


            print(fact_3(9442424594444))