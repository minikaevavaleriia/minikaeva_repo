from zombie_story_game.items.item import *


class Wood(Item):
    def __init__(self, name, addable, interactive):
        super().__init__(name, addable, interactive)

    def action(self, player):
        print('"О, а тут прилично досок, наверное, даже хорошо, что мы так и не починили крышу в прошлом году."')
        print()
