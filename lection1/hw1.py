print('Введите число от 1 до 7, в соответствии с днем недели: ')
mon_fri = [1,2,3,4,5]
sat_sun = [6,7]
a = int(input())

if a in mon_fri:
    print (a, '-> нет')
elif a in sat_sun:
    print (a, '-> да')
else:
    print ('Ошибка: необходимо ввести цифру от 1 до 7')