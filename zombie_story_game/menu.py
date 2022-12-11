import re

from zombie_story_game.heroes.hero import Hero
from zombie_story_game.items.items_in_room.cooker import Cooker
from zombie_story_game.items.items_in_room.cupboard import Cupboard
from zombie_story_game.items.items_in_room.hummer import Hummer
from zombie_story_game.items.items_in_room.jam import Jam
from zombie_story_game.items.items_in_room.nails import Nails
from zombie_story_game.items.items_in_room.photoalbum import Photoalbum
from zombie_story_game.items.items_in_room.window import Window
from zombie_story_game.items.items_in_room.wood import Wood
from zombie_story_game.locations.location import Location


def rules():
    """Тут типа приветики-пистолетики. Добро пожаловать в Зомбилэнд!!!
        Предлагаем вам пройти квест-игру. Просто следуйте инструкциям и помните, сальто вряд ли спасет вас от смерти)))
        Если возникают вопросы в любой момент пишите 'мозги', но мы вам не советуем.
        Если вы умираете, то начинаете все заново, enjoy!

        Донатить разрешается"""
    pass


def initialize_items_in_room():
    nails = Nails('гвозди', True, False)
    jam = Jam('джем', False, True, 20)

    hummer = Hummer('молоток', True, False)
    window = Window('окно', False, True)
    woods = Wood('доски', False, True)
    cooker = Cooker('духовка', False, True)
    photo_album = Photoalbum('фотоальбом', False, True)
    cupboard = Cupboard('шкаф', False, True, [jam, nails])

    items_in_room = [cupboard, cooker, hummer, nails, woods, window, photo_album]
    return items_in_room


def dict_from_items_to_choose(): # создать словаааарь, чтобы вводили цифры и получали конкретный предмет и экшен от него в другой функции
    pass


def initialize_hero():
    user_input = input('Как тебя зовут, борец?\n')
    return Hero('Lera', 80, 20, [], [], [])


def level1():
    pass


def initialize_location1():
    return Location('room',
                    "You're home. Broke and extremely hungry. There are two cupboards, a shelf with photo album "
                    "and a cooker", initialize_items_in_room(), [], [])


def game():
    help(rules)
    while True:
        user_input = input('Введите, что хотите сделать (ввести нужно только слово с маленькой буквы, НЕ ЦИФРУ!!!):\n'
                           '1. Exit\n'
                           '2. Play\n')
        if re.match(r'[(P|p)lay]', user_input) is not None:
            player1 = initialize_hero()
            room = initialize_location1()
            room.observe_room()
            break
        elif re.match(r'[(E|e)xit]', user_input) is not None:
            break
        else:
            print('Введите опцию из меню!!!')
            print()


game()
