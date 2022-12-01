# 5. Рубли

from pytils import numeral

def wordPubles(x):

    word = numeral.choose_plural(x, u"рубль, рубля, рублей")

    print(x, word)


x = int(input("число - "))
wordPubles(x)