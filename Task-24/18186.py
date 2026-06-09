from re import finditer
with open(r'./files/24_18186.txt') as file:
    data=file.readline()
G=r'[AE]'
S=r'[BCDFGH]'
pattern=rf'(?<={S}{S}{G}).+?(?={S+S+G})'