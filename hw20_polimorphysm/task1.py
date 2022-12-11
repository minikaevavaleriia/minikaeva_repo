"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class Person:

    def krya_krya(self):
        print('Типа крякаю')

    def wear_clothes(self):
        print('Чекайте, я в штанах!!!')


class Duck:

    def krya_krya(self):
        print('КРЯ-КРЯ-КРЯ!!!')

    def wear_clothes(self):
        print('Я утка в галстуке!!! КРЯЯЯЯЯЯ!')


def main():
    my_list = [Person(), Duck()]
    for i in my_list:
        i.krya_krya()
        i.wear_clothes()


main()


