'''Как найти сумму элементов списка, более простой способ'''
N = int(input('Введите кол-во элементов списка: '))
print('Введите элементы списка: ')
ages = []
for i in range(N):
    ages.append(int(input()))
print('Итоговый список: ', ages)
print('Сумма элементов массива: ', sum(ages))