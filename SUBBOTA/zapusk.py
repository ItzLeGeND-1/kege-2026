# print('hello',file=open('test.txt','w'))

# Функция для открытия потока на работу с файлом
file = open('test.txt','r')
# readline() - метод считывания одной строки из файла
# возвращает str
data1=file.readline()

# readlines() - метод считывания всех строк из файла
# возвращает список строк - list
# data2=file.readlines()
# print(data2)

# read() - метод для считывания всего файла целиком в одну строку
# Возвращает str
data3=file.read()

# close() - метод для закрытия потока. Пишется после окончания взаимодействия с файлом
file.close()

# Конструкция with as позволяет автоматически закрывать поток при выходе из неё
with open('test.txt') as file:
    data=file.readlines()

print(data)