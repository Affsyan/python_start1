"""
https://drive.google.com/file/d/1IlGcspRcFtXHWA3Yr7ZmX4bR1ZeN46X7/view
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

a = int(input('Введите 3х значное число: '))
n1 = a % 10
n2 = a % 100 // 10
n3 = a // 100

sum_n = n1 + n2 + n3
compos_n = n1 * n2 * n3
print(f"Сумма чисел равна: {sum_n}")
print(f"Произведение чисел равно: {compos_n}")
