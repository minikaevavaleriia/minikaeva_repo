from zombie_story_game.items.item import Item


class Nails(Item):
    def __init__(self, name, addable, interactive):
        super().__init__(name, addable, interactive)
