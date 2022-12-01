# Задача 4. ПИРАМИДА ИЗ ЦИФР

def CheckNumber():
    """Проверяет диапозон числа [1, 9]"""

    num = int(input("Введите число: "))
    while True:
        if 1 <= num <= 9:
            break
    return num

def СentralPyramidNumber(floor):
    """Строит пирамиду чисел
             1
            222
           33333
          4444444
         555555555
        66666666666
       7777777777777
      888888888888888
     99999999999999999
    
    (Не по заданию)
    """
    num = 1
    for i in range(floor):
        print('%s%s' % (' ' * (floor-i-1), f"{num}" * (i*2+1)))
        num += 1

def BinaryPyramidNumber(floor):
    """Строит пирамиду чисел
            _ - пробел
            _____1_____ 
            ____2_2____
            ___3_3_3___
            __4_4_4_4__
            _5_5_5_5_5_
            6_6_6_6_6_6

    """
    space = 10
    num = 1
    stringFloor = ""
   # strCycl = "_" + str(num)
    for i in range(floor):
        stringFloor += " " * space + str(num)
        stringFloor += (" " + str(num)) * i 
        print(stringFloor)
        stringFloor = ""
        num += 1
        space -= 1

# Задача 5. КВАДРАТ

def SquareNamber(num):
    stringFloor = str(num)
    for i in range(num):
        print(stringFloor* num)



while True:
    print("[1] Вывести пирамиду чисел вариант №1\n[2] Вывести пирамиду чисел вариант №2\n[3] Вывести квадрат\n [0] Выйти\n")

    variant = int(input("№ - "))

    if variant == 0:
        break
    elif variant == 1:
        BinaryPyramidNumber(CheckNumber())
    elif variant == 2:
        СentralPyramidNumber(CheckNumber())
    elif variant == 3:
        SquareNamber(CheckNumber())
    else: print("попробуйте ещё раз")  