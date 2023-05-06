'''Как найти сумму элементов списка'''
N = int(input('Введите кол-во элементов списка: '))
print('Введите элементы списка: ')
ages = []
for i in range(N):
    ages.append(int(input()))
print('Итоговый список: ', ages)
summa = 0
for ii in range(N):
    summa += ages[ii]
print(summa)