from zombie_story_game.items.item import Item


class Jam(Item):
    surprise = 0

    def __init__(self, name, addable, interactive, fill_energy):
        super().__init__(name, addable, interactive)
        self.__fill_energy = fill_energy

    def action(self, player):
        print('Вкусно, но грустно... Половина банки джема не восполнит всю энергию, даст только + 20 очков.')
        while True:
            print('Будешь делиться джемом с Билли? Тогда каждому достанется по 10 очков здоровья')
            user_input = str(input('Введите "да" или "нет"?\n'))
            if user_input == 'да':
                player.set_health(player.get_health + self.__fill_energy / 2)
                print('Этот выбор повлияет на будущее!')
                break
            else:
                player.set_health(player.get_health + self.__fill_energy)
                print('Этот выбор повлияет на будущее')
                break