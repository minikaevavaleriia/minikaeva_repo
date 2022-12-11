# classwork
# 1
def music_recommendation():
    for i in range(0, 3):
        print("Введите предпочтение", i + 1)
        user_input = input()
        print("Предпочтение ", user_input, " учтено")
    print("Система рекомендаций настроена!")


music_recommendation()


# 2
def game():

    while True:
        user_input = input('enter smth')
        if user_input != 'off':
            if user_input == 'game':
                print('Угадай число')
                for i in range(0, 3):
                    user_guess = input()
                    if user_guess == '5':
                        print('Вы выиграли билет на концерт!')
        else:
            break


game()


# 3
def login():
    forbidden = '?*^$№@_'
    while True:
        user_input = input('Enter login')
        for i in user_input:
            if i in forbidden:
                print(i)


login()


# 4
def task_4():
    while True:
        user_input = input()
        if user_input != 'off':
            print('Спасибо, ваш отзыв принят!')
        else:
            print('Система предпочтений настроена')
            break


task_4()


# 5
def price_counter():
    while True:
        price = int(input('Enter price'))
        if price != 0:
            price_discount = price / 2
            print('Price with discount: ', price_discount)
        else:
            break


price_counter()


#homework еще не доделала ))))
#6
while True:
    sum_ = 0
    price = int(input('price'))
    if price != 0:
        if price % 2 == 0:
            sum_ += price
        else:
            print('Total: ', price * 0.85)
    else:

        break






