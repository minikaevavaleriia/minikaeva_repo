"""
Даны два списка чисел. Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
"""


def task1(_list1, _list2):
    print(sorted(set(_list1).intersection(set(_list2))))


list1 = [1,2,3,4,5,6]
list2 = [4,16,1,3,8,2]
task1(list1, list2)


"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""


def task2(_list):
    printSet = set()
    for element in _list:
        if type(element) == list or type(element) == dict or type(element) == set:
            _list.remove(element)
        else:
            printSet.add(element)
    if len(printSet) > 0:
        print(True)
        print(_list)
    else:
        print(False)


testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
task2(testList)


"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
_newspaper = range(1, 76)
_magazine = range(77, 104)
_both = range(21, 34)


def task_3(newspaper, magazine, both):
    only_newspaper = (set(newspaper)).difference(set(both))
    only_magazines = (set(magazine)).difference(set(both))
    print(len(only_magazines) + len(only_newspaper) + len(both))


task_3(_newspaper, _magazine, _both)


"""
Вася давно мечтает выиграть олимпиаду по информатике.
У него всего три слабых места: циклы, массивы и строки.
Перед сегодняшним турниром Вася провёл интенсивную подготовку, в ходе которой он решил A задач на циклы,
B задач на массивы и C задач на строки.
Впоследствии выяснилось, что из решённых задач D были и на циклы, и на массивы, E – на циклы и на строки,
F – на строки и на массивы. И даже было G задач, которые включали и циклы, и строки, и массивы.
Помогите Васе вычислить, сколько всего различных задач он решил.
Введите результат для всех 3 входных данных
"""


first_ = "0 0 0 0 0 0 0" #Вывод должен быть 0
second_ = "1 1 1 0 0 0 0" # Вывод должен быть 3
third_ = "1 1 1 1 1 1 1" # Вывод должен быть 1


def task_4(first, second, third):
    A, B, C, D, E, F, G = map(int, first.split())
    print(A + B + C - F + D + E - G)
    A, B, C, D, E, F, G = map(int, second.split())
    print(A + B + C - F + D + E - G)
    A, B, C, D, E, F, G = map(int, third.split())
    print(A + B + C - (F + D + E - G))


task_4(first_, second_, third_)



"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""


n = int(input())
d = {}
intersect = set()
count, amount = 0, 0
while count != n:
    m = int(input())
    vsp = set()
    lang = input().split()
    for i in lang:
        d.setdefault(m, []).append(i)
        vsp.add(i)
    if count == 0:
        intersect |= vsp
        amount = m
    elif intersect & vsp != set():
        intersect &= vsp
        if amount > m:
            amount = m
    count += m
otv = set()

for i in d.values():
    for j in i:
        otv.add(j)
print(list(otv))
print(f'{amount} - {list(intersect)}')
