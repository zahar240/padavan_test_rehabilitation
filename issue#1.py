"""
Написать функцию, которая определяет, является ли слово палиндромом.

Палиндро́м — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях.

Примеры: 101, топот, saippuakivikauppias, а роза упала на лапу Азора
"""




def polindrom(x):
    x = x.lower().replace(" ","")
    return x == x[::-1]
    

print(polindrom("101"))
print(polindrom("saippuakivikauppias"))
print(polindrom("а роза упала на лапу Азора"))

