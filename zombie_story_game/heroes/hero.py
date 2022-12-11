class Hero:

    def __init__(self, name, health, energy, weapons, items, checked_locations):
        self.__name = name
        self.__health = health
        self.__energy = energy
        self.__weapons = weapons
        self.__items = items
        self.__checked_locations = checked_locations

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_energy(self):
        return self.__energy

    def set_energy(self, energy):
        self.__energy = energy

    def get_weapons(self):
        return self.__weapons

    def set_weapons(self, *args):
        for w in args:
            self.__weapons.append(w)

    def get_items(self):
        return self.__items

    def set_items(self, *args):
        for item in args:
            self.__items.append(item)

    def get_checked_locations(self):
        return self.__checked_locations

    def set_checked_locations(self, *args):
        for loc in args:
            self.__checked_locations.append(loc)

    def remove_item(self, item):
        self.__items.remove(item)
        print(f'{item.get_name().capitalize()} успешно выкинут из рюкзака')

    def print_items(self):
        print('В рюкзаке:')
        i = 1
        for item in self.get_items():
            print(f'{i}. {item.get_name().capitalize()}')
            i += 1

    def add_item(self, item):
        if item.get_interactive and item not in self.get_items():
            self.__items.append(item)
            print(f'{item.get_name().capitalize()} успешно добавлен в рюкзак')
        else:
            print(f'Нельзя добавить {item.get_name()} предмет в рюкзак')
            pass

    def item_action(self, item):
        if item.get_interactive():
            item.action(self)
        else:
            print(item.IF_NOT_INTERACTIVE)

    def checkout(self):
        print(f'Игрок {self.get_name()}\n'
              f'Здоровье: {self.get_health()}\n'
              f'Энергия: {self.get_energy()}\n')
        self.get_items()

