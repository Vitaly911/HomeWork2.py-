s = int(input('Введите сумму чисел: '))  # 5
p = int(input('Введите произведение чисел: '))  # 6
i = 1
deL = 0
count = 0
while (i < s):
    if (p % i == 0):
        deL = p // i
        if (deL + i == s):
            print(deL)
            print(i)
            count += 1
            i = s
    i += 1
if(count == 0):    
    print("Введены не корректные данные")