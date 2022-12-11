class Item:
    IF_NOT_INTERACTIVE = ''

    def __init__(self, name, addable, interactive):
        self.__name = name
        self.__addable = addable
        self.__interactive = interactive

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_addable(self):
        return self.__addable

    def set_addable(self, addable):
        self.__addable = addable

    def get_interactive(self):
        return self.__interactive

    def set_interactive(self, interactive):
        self.__interactive = interactive

    def action(self, player):
        print('act!')
