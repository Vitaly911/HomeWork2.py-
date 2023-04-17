number = int(input('Введите количество монет: '))
i = 0
eagle = 0
tails = 0
while (i < number):
    coin = int(input('Введите монету (1 или 0): '))
    if (coin != 1 and coin != 0):
        print("Введите число 0 или 1")
    else:
        if (coin == 1):
            eagle += 1
        else:
            tails += 1
        i += 1
if (eagle < tails):
    min = eagle
else:
    min = tails
print(min)