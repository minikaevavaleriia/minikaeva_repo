from zombie_story_game.heroes.hero import Hero
from zombie_story_game.items.items_in_room.cooker import *
from zombie_story_game.items.items_in_room.cupboard import *
from zombie_story_game.items.items_in_room.hummer import Hummer
from zombie_story_game.items.items_in_room.jam import Jam
from zombie_story_game.items.items_in_room.nails import Nails
from zombie_story_game.items.items_in_room.window import Window
from zombie_story_game.items.items_in_room.wood import Wood
from zombie_story_game.locations.location import *

# initializing items
nails = Nails('гвозди', True, False)
hummer = Hummer('молоток', True, False)
window = Window('окно', False, True)
woods = Wood('доски', False, True)
cooker = Cooker('духовка', False, True)
jam = Jam('джем', False, True, 20)
cupboard = Cupboard('шкаф', False, True, [jam, nails])


# initializing locations
room1 = Location('room', "You're home. Broke and extremely hungry. There are two cupboards, a shelf with photo album "
                         "and a cooker", [cupboard, cooker, hummer, nails, woods], [], [])


# initializing heroes
player1 = Hero('Lera', 80, 20, [], [hummer, nails], [])
# window.action(player1)

# testing

# print(player1.get_name(), player1.get_health())
player1.print_items()
cupboard.print_cupboard()
# #
# room1.observe_room(room1)
# cooker.action(player1)
# cupboard.action(player1)
#
# print(player1.get_health())
# print(player1.get_energy())
