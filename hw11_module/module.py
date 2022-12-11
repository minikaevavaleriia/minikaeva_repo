import re
from random import *
from time import *


class Autoresponse:
    SPORT_TIMETABLE = 'Monday:\n10:00 - youga\n12:00 - crossfit\nFriday:20:00 - crossfit\n22:00 - yoga'
    COACH_NUMBER = 'Контакт тренера:\n89995067783\nФролов Андрей Александрович'
    BASIC_PRICE = 2000
    ADVANCED_PRICE = 4000
    CARTOON1 = 'Рик и Морти'
    CARTOON2 = 'С приветом по планетам'
    CARTOON3 = 'Симпсоны'
    JOKE = 'Повар спрашивает повара...'
    JOKE1 = '- Сколько бит содержится в "инте"?'
    JOKE2 = '- А мне-то откуда знать, я в колледж Сириус по приколу поступал!!!'

    def __init__(self, request=None):
        self.__request = request

    def get_request(self):
        return self.__request

    def set_request(self, request):
        self.__request = request

    def user_input(self):
        pattern1 = r'.*(\bраспис*|\bРаспис*)'
        pattern2 = r'.*(\bтренер.*|\bТренер.*\b)'
        pattern3 = r'.*(\bоплат*|\bОплат*|\bцен*|\bстоимост*|\bСтоимост*|\bЦен*)'
        pattern4 = r'.*(\bмульт*|\bМульт*)'
        pattern5 = r'.*(\bшутк*|\bанекдот*|\bприкол*|\b Анекдот*|\bПрикол*|\bШутк*)'
        if re.match(pattern1, self.get_request()) is not None:
            print(self.SPORT_TIMETABLE)
        if re.match(pattern2, self.get_request()) is not None:
            print(self.COACH_NUMBER)
        if re.match(pattern3, self.get_request()) is not None:
            ask_user = input('Укажите ваш тариф. 1 - базовый. 2 - супермегаплюспро: ')
            if ask_user == '1':
                print(self.BASIC_PRICE)
            elif ask_user == '2':
                print(self.ADVANCED_PRICE)
            else:
                print('Такого тарифа нет, свяжитесь с тренером')
                print(self.COACH_NUMBER)
        if re.match(pattern4, self.get_request()) is not None:
            var = randint(1, 3)
            if var == 1:
                print(self.CARTOON1, 'или', self.CARTOON2)
            else:
                print(self.CARTOON3)
        if re.match(pattern5, self.get_request()) is not None:
            print(self.JOKE)
            sleep(1)
            print(self.JOKE1)
            sleep(2)
            print(self.JOKE2)
