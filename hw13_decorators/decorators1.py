from time import *


def decorate(func):
    time_start = time()
    func_to_decor()
    time_end = time()
    print('Время выполнения:')
    print(time_end - time_start )


def func_to_decor():
    for i in range(1000):
        print(i)


def main():
    decorate(func_to_decor())


main()
