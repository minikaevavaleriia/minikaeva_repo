from zombie_story_game.items.item import *
from zombie_story_game.items.items_in_room.hummer import Hummer
from zombie_story_game.items.items_in_room.nails import Nails
from zombie_story_game.items.items_in_room.wood import Wood


class Window(Item):
    def __init__(self, name, addable, interactive):
        super().__init__(name, addable, interactive)

# вызывать метод после взгляда в окно и осмотра досок в комнате, Билли может сам предложить заколотить окно
    def action(self, player):
        if any(isinstance(x, Hummer) for x in player.get_items()):
            if any(isinstance(x, Nails) for x in player.get_items()):
                while True:
                    print('Заколотить окно?\n')
                    user_input = str(input('Введите "да" или "нет"?\n'))
                    if user_input == 'да':
                        print('Окно успешно заколочено!\n')
                        break
                    else:
                        print('Билли: я настаиваю на том, чтобы мы заколотили окно, иначе нас сожрут!!!\n')
            else:
                print('Тебе нужны гвозди!\n')
        else:
            print('Тебе нужен молоток!\n')


