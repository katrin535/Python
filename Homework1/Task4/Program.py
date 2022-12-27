#Напишите программу, которая по заданному номеру четверти показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))

def diapazon(number):
    if number > 4 and number <= 0:
        print('Ошибка: Введите число от 1 до 4')
    elif number == 1:
        print('Диапазон для I четверти: x>0 y>0')
    elif number == 2:
        print('Диапазон для II четверти: x<0 y>0')
    elif number == 3:
        print('Диапазон для III четверти: x<0 y<0')
    elif number == 4:
        print('Диапазон для IV четверти: x>0 y<0')
    else:
        print('Введите число')

diapazon(number)