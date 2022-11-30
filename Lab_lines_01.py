# 1. Палиндром

def is_palindrome(line):
    print(line)
    r_line = line[::-1]
    return line == r_line


line = str(input("Введите строку - "))
line = line.lower()
symbols = "!?-+* .,':;="

for i in range(len(symbols)):
    line = line.replace(symbols[i], "")
    #  print(line)

print(is_palindrome(line))
