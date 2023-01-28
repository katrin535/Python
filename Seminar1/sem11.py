#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = int (input('Введите число a: '))
b = int (input('Введите число b: '))
c = int (input('Введите число c: '))
d = int (input('Введите число d: '))
e = int (input('Введите число e: '))

max = a

if (b>max):
    max = b
elif (c>max):
    max = c
elif (d>max):
    max = d
elif (e>max):
    max = e

print('Максимальное число:' , max)