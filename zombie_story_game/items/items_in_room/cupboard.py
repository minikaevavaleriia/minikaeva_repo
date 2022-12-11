from zombie_story_game.items.item import *


class Cupboard(Item):
    IF_NOT_INTERACTIVE = 'Вы открыли шкаф, но там пусто'

    def __init__(self, name, addable, interactive, food):
        super().__init__(name, addable, interactive)
        self.__food = food

    def get_food(self):
        return self.__food

    def set_food(self, *args):
        for f in args:
            self.__food.append(f)

    def print_cupboard(self):
        i = 1
        print('В шкафу есть:')
        for f in self.__food:
            print(f'{i}. {f.get_name().capitalize()}')
            i += 1

    def action(self, player1):
        print(f'Вы открыли {self.get_name()} и нашли...')
        if self.__food:
            self.print_food()
        else:
            print('горы паутины, брррр... Нужно поискать еще')
