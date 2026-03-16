with open('путь до файла') as file:
    #Считывает весь файл. Возвращает str
    data=file.read()
    #считывает одну строку до символа \n Возвращает str
    data=file.readline()
    # считывает все строки. Возвращает list[str]
    data = file.readline()