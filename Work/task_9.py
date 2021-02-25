"""
https://drive.google.com/file/d/1ceHOXTJZxRcVZxzclb2E33mYugvsOrFx/view?usp=sharing
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

a = int(input("Введите 1вое число: "))
b = int(input("Введите 2рое число: "))
c = int(input("Введите 3тье число: "))

if ((a > b) and (a < c)) or ((a < b) and (a > c)):
    print(a)
elif ((c > b) and (c < a)) or ((c < b) and (c > a)):
    print(c)
else:
    print(b)
