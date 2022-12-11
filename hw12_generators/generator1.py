"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""


def generator1(s):
    for i in s:
        if i.isalpha():
            yield i


def main():
    g1 = generator1('234he""l456*&lo678 every o_n+e~!')

    for el in g1:
        print(el)


main()

