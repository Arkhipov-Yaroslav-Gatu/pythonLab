# 2. Таблица умножения
  

def get_table(multipliTwo):
    """ 
    list[j] * list[i+1] = list[j]*list[i+1]
    """

    stringMulti = ''
    listMultipliersb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # тут код для генерации строки по двум параметрам
    # s = '1\t2\t3\n1\t4\t9\n'  # например, получилась такая строка
    for i in range(10):
        stringMulti += f"{listMultipliersb[i]} * {listMultipliersb[multipliTwo]} = {listMultipliersb[i] * listMultipliersb[multipliTwo]}\n"
    # print(stringMulti)
    return stringMulti

listTable = []
for i in range(9):
    listTable.append(get_table(i))
    
output = "".join(listTable)
print(output)