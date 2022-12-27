print('Введите a: ')
a = input()
print('Введите b:')
b = input()
print('a и b =')
print(f'{a},{b}')


print('Введите a: ')
a = float(input())
print ('Введите b: ')
b = float(input())
print (a, ' + ', b , ' = ', a+b)

a = 13
b = 20
c = a // b
print ('Деление без остатка с = ', c) 

a = 2
b = 32
c = round(a ** b, 3)
print ('Число a в степени b, округленное до 3-х знаков после запятой = ', c) 

a = 2
a *=3  #сокращенная операция присваивания

a = 1 < 4
print(a)   #выводит true или false

a = 1 < 3 < 5 < 8  # четверные неравества
print(a) 

a = 1
b = 2
c = 3
print(a<b<c) # вывести логическую операцию тройного неравества

