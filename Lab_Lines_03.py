# 4. Гласная-Согласная


def definedLine(line):
    lineSoglasn = line
    glasn = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю','я', 'ь', 'ъ']
    for i in range(len(glasn)):
        line = line.replace(glasn[i], "")
        
    print(lineSoglasn, " - ", line)

    if len(lineSoglasn) % len(line) == 0:   
        print("Гласных и согласных поровну")
    elif len(lineSoglasn) > len(line):
        print("гласных меньше чем согласных") 
    else: 
        print("Согласных меньше чем гласных")   

word = input()

definedLine(word)