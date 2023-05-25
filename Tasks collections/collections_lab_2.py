import math

digits = {  # это словарь образов цифр
    0: ('XXX', 'X X', 'X X', 'X X', 'XXX'),
    1: ('  X', ' XX', 'X X', '  X', '  X'),
    2: ('XXX', '  X', 'XXX', 'X  ', 'XXX'),
    3: ('XXX', '  X', 'XXX', '  X', 'XXX'),
    4: ('X X', 'X X', 'XXX', '  X', '  X'),
    5: ('XXX', 'X  ', 'XXX', '  X', 'XXX'),
    6: ('XXX', 'X  ', 'XXX', 'X X', 'XXX'),
    7: ('XXX', '  X', ' X ', ' X ', ' X '),
    8: ('XXX', 'X X', 'XXX', 'X X', 'XXX'),
    9: ('XXX', 'X X', 'XXX', '  X', 'XXX')
}

def get_number():
    string_numbers =''
    number = int(input("Enter Number: "))
    list_number = [(number//(10**i))%10 for i in range(math.ceil(math.log(number, 10))-1, -1, -1)] 
    for j in range(5):
        for i in range(len(list_number)):
            dig = digits[list_number[i]]
            string_numbers += dig[j] + "  "
        print(string_numbers)
        string_numbers = ""

 
get_number()