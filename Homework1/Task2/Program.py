#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введите X: '))
Y = int(input('Введите Y: '))
Z = int(input('Введите Z: '))
notXYZ = not X and not Y and not Z

if not (X or Y or Z) == notXYZ:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')


