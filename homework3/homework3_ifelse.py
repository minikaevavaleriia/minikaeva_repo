# 1
def task_1(choice):
    if choice == '1':
        print('Ешь кашу мэн')
    else:
        print('Хочешь плотно поесть? Пиши "да" или "нет"')
        if input() == 'да':
            print('Ешь плов')
        else:
            print('Ешь котлету с пюре')


task_1(input('1.завтрак 2.обед 3.ужин?'))


# 2
def task_2(price):
    time_hours = int(input('Сколько сейчас часов (без минут)? 24-часовой формат!!!'))
    if 10 <= time_hours <= 12:
        print('цена теперь: ', price / 2)
    elif 20 <= time_hours <= 22:
        print('цена теперь: ', price / 4)
    else:
        print('цена теперь: ', price)


task_2(int(input('Сколько стоит товар?')))


# 3
def task_3():
    items_list = []
    for i in range(0, 3):
        print('Введите стоимость ', i + 1, 'товара')
        items_list.append(int(input()))
    for i in range(0, 1):
        if (items_list[i] < items_list[i+1]) and (items_list[i+1] < items_list[-1]):
            price = sum(items_list) / 2
            print('Акция!', price)
        elif (items_list[i] > items_list[i+1]) and (items_list[i+1] > items_list[-1]):
            price = sum(items_list) / 3
            print('Акция!', price)
        else:
            print('К оплате: ', sum(items_list))


task_3()


# 4
def task_4(item_category):
    if item_category == 'продукты':
        price = int(input('Введите цену'))
        if price < 100:
            print('Попробуйте нашу выпечку!')
        if (price >= 100) and (price < 500):
            print('Как насчёт орехов в шоколаде?')
        if price >= 500:
            print('Попробуйте экзотические фрукты!')
    else:
        print('Загляните в товары для дома!')


task_4(input('Введите категорию'))


# 5
def task_5(n):
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    return summ


num = int(input())
if ((num % 10) % 2 == 0) and task_5(str(num)) % 3 == 0:
    print('Да делится')
else:
    print('Не делится')

