"""
https://drive.google.com/file/d/1G5JB7w9cHXpb5ZX5ATMjcM4d0KEp_CbE/view?usp=sharing
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

bit_or = 5 | 6
bit_and = 5 & 6
bit_xor = 5 ^ 6

left_shift = 5 << 2
shift_right = 5 >> 2

print(f'Побитовое or для 5 и 6: {bit_or}')
print(f'Побитовое and для 5 и 6: {bit_and}')
print(f'Побитовое xor для 5 и 6: {bit_xor}')
print(f'Побитовый сдвиг влево на 2 знака: {left_shift}')
print(f'Побитовый сдвиг вправо на 2 знака: {shift_right}')
