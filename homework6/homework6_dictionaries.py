"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""

print('Задание 1')


def create_dict():
    power_of_number = 2
    dictionary = dict()
    for i in range(1, 11):
        dictionary[i] = pow(i, power_of_number)
    print(dictionary)


create_dict()


"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""


print('Задание 2')


def key_number_value_amount(numbers):
    list_of_numbers = []
    list_of_amount_of_numbers = []
    dict_ = dict()
    for i in range(0, len(numbers)):
        list_of_numbers.append(int(numbers[i]))
    for x in set(list_of_numbers):
        if numbers.find(str(x)) != -1:
            list_of_amount_of_numbers.append(list_of_numbers.count(x))
    j = 0
    for x in set(list_of_numbers):
        dict_[x] = list_of_amount_of_numbers[j]
        j += 1
    print(dict_)


numbers_ = "0139412831055230677798"
key_number_value_amount(numbers_)


"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""


print('Задание 3')


def music_chart():
    dict_ = {}
    while input != 'off':
        place = input('Введите место в чарте: ')
        if place != 'off':
            singer = input('Введите исполнителя: ')
            if singer != 'off':
                name = input('Введите название: ')
                if name != 'off':
                    if place and singer and name:
                        dict_[place, singer] = name
                else:
                    print(dict_)
            else:
                print(dict_)
        else:
            print(dict_)
    print(dict_)


music_chart()


"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""


print('Задание 4')


def change_dictionary(my_dict):
    buffer_value1 = my_dict[1]
    my_dict[1] = my_dict[5]
    my_dict[5] = buffer_value1
    del my_dict[2]
    my_dict['new_key'] = 'new_value'
    print(my_dict)


dict_ = {1: 'a',
         2: 'b',
         3: 'c',
         4: 'd',
         5: 'e'}
change_dictionary(dict_)


"""
Дан словарь email-адресов студентов, в качестве ключа используется домен, а в качестве значения список имен.
Необходимо вывести все email-адреса в формате Имя@домен.
"""


print('Задание 5')


def emails(mails):
    keys = list(mails.keys())
    values = list(mails.values())
    symbol = '@'
    try:
        for i in range(0, len(keys[0]) - 1):
            print(values[0][i] + symbol + keys[0])
    except IndexError:
        pass
    try:
        for i in range(0, len(keys[1])):
            print(values[1][i] + symbol + keys[1],
                  values[2][i] + symbol + keys[2],
                  values[4][i] + symbol + keys[4],
                  values[5][i] + symbol + keys[5])
    except IndexError:
        pass
    try:
        for i in range(0, len(keys[3]) - 1):
            print(values[3][i] + symbol + keys[3])
    except IndexError:
        pass


my_emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
             'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
             'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
             'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
             'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
             'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
emails(my_emails)




