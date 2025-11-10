#Системы счисления
N=25
#Перевод десятичное число в двоичную система
#Принимает на вход int, возвращает str
#[2:]- срез, убирающий первые два символа 'ob'
print(bin(N)[2:])
#f'' -  форматируемая строка, которая повзоляет вставлять в себя переменные
print(f'{N:b}')

# Восьмеричная система
print(oct(N)[2:])
print(f'{N:o}')

#Шестнадцатеричная система
print(hex(N)[2:])
print(f'{N:x}')

#перевод в троичную систему
k=""
while N>0:
    k=str(N%3)+k
    N//=3
print(k)


# Перевод в любую систему счисления (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    # Пока целая часть не ноль, продолжаем делить
    while num != 0:
        # Получаем остаток, приписываем к результату
        res += str(num % sys)
        # Получаем новую целую часть
        num //= sys
    # Переворачиваем строку (записываем остатки в обратном порядке)
    return res[::-1]

# Перевод в любую систему (2 <= sys <= 36)
from string import printable as alph

def convert2(num,sys):
    res = ''
    while num !=0:
        res+= alph[num%sys] #res+= printable[num%sys]
        num//=sys
    return res[::-1]

#перевод в десятичную систему
num_bin='101'
num_tri='201'
num_hex='f01'
print(int(num_bin,2))
print(int(num_tri,3))
print(int(num_hex,16))