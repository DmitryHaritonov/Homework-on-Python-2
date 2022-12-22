def RandomArray(n) :
    import random
    m = []
    moneyUp = 0
    for i in range(0, n) :
        randoms_num = round(random.randint(0, 1))
        m.append(randoms_num)
    return m
#----------------------------------------
num = int(input('Введите кол-во монет:'))
array = RandomArray(num)
print(array)

moneyDown = 0
#----------------------------------------

for i in array:
    if i == 0:
        moneyDown = moneyDown + 1
#=========================================
moneyUp = len(array) - moneyDown
print(moneyDown)
print(moneyUp)
#-----------------------------------------
if moneyDown < moneyUp:
    print('Перевернуть нужно:', moneyDown)
elif moneyDown == 0 or moneyUp == 0:
    print('Все монеты лежат на столе одной стороной ')
else :
    print('Перевернуть нужно:',moneyUp)     