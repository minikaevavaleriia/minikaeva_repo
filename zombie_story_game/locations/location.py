class Location:

    def __init__(self, name, description, interact_items, non_interact_items, checked):
        self.__name = name
        self.__description = description
        self.__interact_items = interact_items
        self.__non_interact_items = non_interact_items
        self.__checked = checked

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_interact_items(self):
        return self.__interact_items

    def set_interact_items(self, *args):
        for w in args:
            self.__interact_items.append(w)

    def get_non_interact_items(self):
        return self.__non_interact_items

    def set_non_interact_items(self, *args):
        for item in args:
            self.__non_interact_items.append(item)

    def get_checked(self):
        return self.__checked

    def set_checked(self, checked):
        self.__checked = checked

    def observe_room(self):
        print(f'Вы оказались в локации:{self.get_name()}')
        print(self.get_description())
        print('Введите номер предмета, который хотите рассмотреть поближе')
        self.show_all_items_in_location()

    def show_all_items_in_location(self):
        all_items = self.__interact_items + self.__non_interact_items
        i = 1
        for item in all_items:
            print(f'{i}. {item.get_name().capitalize()}')
            i += 1
        return all_items

    # def define_chosen_item(self, player):



