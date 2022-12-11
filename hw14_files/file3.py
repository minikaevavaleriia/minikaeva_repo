"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""


def file3():
    name_1 = input('Enter first file name: ')
    name_2 = input('Enter first file name: ')
    full_name1 = '/home/sirius/text_files_for_hw/' + name_1
    full_name2 = '/home/sirius/text_files_for_hw/' + name_2
    stack = []
    with open(full_name1, 'r+') as f1:
        for line in f1:
            stack.append(line)
    print(stack)
    with open(full_name2, 'w+') as f2:
        for i in range(0, len(stack)):
            f2.writelines(str(i + 1) + ': ' + stack[i])
    with open(full_name2, 'r+') as f3:
        print(f3.read())


file3()
