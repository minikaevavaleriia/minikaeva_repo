from zombie_story_game.items.item import *


class Cooker(Item):
    IF_NOT_INTERACTIVE = 'Вы открыли духовку, но это ничего не дало'

    def __init__(self, name, addable, interactive):
        super().__init__(name, addable, interactive)

    def action(self, player):
        player.set_health(player.get_health() - 5)
        player.set_energy(player.get_energy() + 60)
        print('Вы обожглись и потеряли 5 очков здоровья, зато ваша энергия пополнилась до 80 очков')
