from re import *
with open(r'./files/24-371.txt') as file:
    data=file.readline()
pattern=r'([^M\.]*M){112}[^M\.]*\.'