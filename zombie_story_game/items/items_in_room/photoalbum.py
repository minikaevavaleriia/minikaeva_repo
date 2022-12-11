from zombie_story_game.items.item import Item


class Photoalbum(Item):
    def __init__(self, name, addable, interactive):
        super().__init__(name, addable, interactive)

    def action(self, player):
        print('Старый фотоальбом скрывал много секретов... Например, тот момент, когда батя ушел за хлебом... Стало '
              'грустно, энергии убавилось аж на 5 единиц. Не лезем туда, куда не нужно :)')
        player.set_energy(player.get_energy() - 5)
