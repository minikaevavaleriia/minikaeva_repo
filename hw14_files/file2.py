"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""


def file2():
    with open('/home/sirius/new_doc_for_hw.txt', 'w+') as f2:
        f2.write('но у меня не получается')
    with open('/home/sirius/join_files.txt', 'w+') as final:
        with open('/home/sirius/file_for_homework.txt', 'r+') as f1:
            with open('/home/sirius/new_doc_for_hw.txt', 'r+') as f2:
                final.write(f1.read() + ' ')
                final.write(f2.read())
    with open('/home/sirius/join_files.txt', 'r+') as final1:
        print(final1.read())


file2()
