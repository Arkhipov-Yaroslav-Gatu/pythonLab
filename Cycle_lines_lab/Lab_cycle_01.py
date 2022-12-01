def is_prime(a):
    """Простое число или нет """

    if a % 2 == 0:
      return a ==  2
    d = 3
    while d * d <= a and a % d != 0:
      d += 2
    return d * d > a    

def nums_prime():
    """Список простых чисел"""
    print([ '{} - Простое'.format(i) for i in range(1, 1001) if is_prime(i)])

def check_perfect(num):
    """"Проверка совершенного числа"""

    sm = 0
    for i in range(1, num):
        if num % i == 0:
            sm += i
    return sm == num    

def get_num():
    """Ввод числа, проверка числа в диапозоне 1 до 1000"""

    a = int(input("Введите число: "))
    while True:
        if 1 <= a <= 1000:
            break
    return a   


while True:
    print(" [1] вывести число и проверить простое или нет,\n [2] вывести список простых чисел,\n [3] вывести совершенное число,\n [0] выйти \n")
    variant = int(input("№ - "))

    if variant == 0:
        break
    elif variant == 1:
        print(is_prime(int(input("Введите число: "))))
    elif variant == 2:
        nums_prime()
    elif variant == 3:
        for num in range(1, 1000):
            if check_perfect(num):
                print(num)
    else: print("попробуйте ещё раз")
