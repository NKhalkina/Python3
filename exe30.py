'''Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an= a1+ (n-1) * d.
Каждое число вводится с новой строки.'''

a=int(input('Введите первый элемент массива a = '))
d=int(input('Введите разность элементов: '))
n=int(input('Введите количество элементо n = '))
for i in range(n):
    print(a+i*d)