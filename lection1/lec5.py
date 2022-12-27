original = 23
inverted = 0 
while original !=0:  #пока не равен 0
    inverted = inverted * 10 + (original % 10)  #переворачиваем число
    original //=10
else:
    print('111')
print(inverted)