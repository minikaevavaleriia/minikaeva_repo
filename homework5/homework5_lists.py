# Напиши программу, запрашивающую ввод настольной игры, пока не введён 0 (сигнал конца ввода). 1. Если такая игра
# уже есть в списке, то должно печататься: «Эта игра уже записана». 2. Если такой игры ещё нет, то игра добавляется в
# список. Список сортируется по алфавиту.


def list_of_games():
    game_list = []
    while True:
        user_input = input('Enter your game')
        if not user_input == '0':
            if user_input in game_list:
                print('Эта игра уже записана')
            else:
                game_list.append(user_input)
        else:
            for game in sorted(game_list):
                print(game)
            break


list_of_games()


# В конце некоторых тренингов подсчитывается успеваемость студентов. Успеваемость — это сумма количества пятёрок,
# четвёрок и троек, поделённая на общее число оценок и умноженная на 100. Пример: Пусть имеются оценки 5, 3, 2,
# 4. Тогда успеваемость: (1 + 1 + 1)/4*100 = 75. Напишите программу выводящую список оценок и список количества
# оценок, а так же успеваемость.


def marks():
    while True:
        str_of_marks = input('Enter all marks with no spaces')
        print("List of marks: " + ', '.join(str_of_marks))
        marks_and_amount = {}
        for mark in sorted(set(str_of_marks)):
            marks_and_amount[mark] = list(str_of_marks).count(mark)
            print('Amount of ', mark, ' is: ', marks_and_amount.get(mark))
        print('Успеваемость: ', (marks_and_amount.get('3') + marks_and_amount.get('4')
                                 + marks_and_amount.get('5')) / len(str_of_marks) * 100)


marks()


# Программа запрашивает набор оценок студента через пробел и считает количество «пятёрок». Зная число «пятёрок» и
# число всех оценок, программа может посчитать процент полученных «пятёрок».


def all_fives():
    while True:
        grades = input()
        amount_of_5 = grades.count('5')
        buffer = grades.split(' ')
        amount_of_all = len(buffer)
        print((amount_of_5 * 100) / amount_of_all)


all_fives()


# Запрограммируй наставникам заполнение личной информации. Программа должна запрашивать ввод: 1. Фамилия
# преподавателя. 2. Должность. 3. Количество студентов во всех группах(например: 12,8,10). Эти данные должны лежать в
# отдельном списке внутри общего списка с информацией.


def teacher_info():
    information_list = []
    while True:
        lastname = input('Lastname: ')
        position = input('Position: ')
        students_all_groups = input('Amount of students: ').split(',')
        new_list = [lastname, position, students_all_groups]
        information_list.append(new_list)
        print(information_list)


teacher_info()


# Напишите программу проверяющую является ли список чисел возрастающим непрерывно. Например для списка [0,1,2,3,4],
# программа должна выводить “Да”, а для списка [0,1,3,4] “Нет”. Для последовательности из 1 числа программа должна
# писать “Нет”.


def check_lists(list1):
    if len(list1) > 1:
        list2 = sorted(list1)
        if list1 == list2:
            print("Да")
        else:
            print("Нет")
    else:
        print("Нет")


_list = [3, 7, 8, 90]
check_lists(_list)
_list1 = [20, 35, 12]
check_lists(_list1)
_list2 = [5]
check_lists(_list2)
