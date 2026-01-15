# Порядок выполнения операций в алгебре логики
# 1. Отрицание / Инверсия (¬A, (not A))
# 2. Логическое умножение / Конъюнкция (A∧B, A∙B, A and B)
# 3. Логическое сложение / Дизъюнкция (A∨B, A+B, A or B)
# 4. Следование / Импликация (A→B, A <= B)
# 5. Тождество / Эквивалентность (A≡B, A == B)

# Исключающее или / XOR (A ⊕ B, A ^ B)

# Порядок выполнения операций в Python
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. in, not in
# 6. ==, !=, >, >=, <, <=
# 7. ^
# 8. not
# 9. and
# 10. or

# Решение через лесенку
print('a b c d')
for a in 0,1:
    for b in range(2):
        for c in (0,1):
            for d in [0,1]:
                F = (not a and not b) or (b==c) or d
                # все строки истинны
                if F:
                    #print(a,b,c,d)
                # все строки ложны
                if not F:
                    print(a,b,c,d)
                # строки в перемешку
                print(a,b,c,d)
from itertools import permutations

def f(x,y,w,z):
    return (x or y and not z) and (not w)
table=[
    (1,0,0,0),
    (0,0,1,0),
    (0,1,0,1)]
for p in permutations('xywz'):
    if [f(**dict(zip(p,t)))for t in table]==[1,1,0]:
        print(*p,sep='')