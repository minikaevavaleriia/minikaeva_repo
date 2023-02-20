"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""
import sys

input_ = sys.argv
a = []

try:
    for i in input_:
        if i.find('--') != -1:
            a.append(input_[input_.index(i) + 1])

    with open(f'/home/sirius/minikaeva_repo/hw24_sys_module/{a[1]}.txt', 'w+') as f:
        f.write(a[0])

except IndexError:
    print('Недостаточно аргументов!!!')