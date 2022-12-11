"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""


def file():
    with open('/home/sirius/file_for_homework.txt', 'w+') as f:
        f.write('Я гений и стараюсь учить питон')
    with open('/home/sirius/file_for_homework.txt', 'r+') as f:
        print((f.read())[0:7])


file()
