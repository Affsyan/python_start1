"""
https://drive.google.com/file/d/1FuelEaazgEPk1Po6OwOc3qbfd3RpXkbo/view?usp=sharing
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""

y = int(input("Введите год: "))

if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    print("Год высокосный")
else:
    print("Год обычный")
