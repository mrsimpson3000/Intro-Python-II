from room import Room
from player import Player
from item import Item

import time

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'sword': Item('sword', 'a rusty sword', 'a well used rusty sword'),
    'debris': Item('debris', 'some debris', 'debris left from earlier adventurers who got here before you'),
    'shield': Item('shield', 'a wooden shield', 'a small shield made from wood. It has seen better days'),
    'backpack': Item('backpack', 'a small backpack', 'a small backpack to carry your inventory in')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Put items in the rooms

room['outside'].items = [items['shield']]
room['foyer'].items = [items['sword']]
room['treasure'].items = [items['debris']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("Please enter your name: ")
player = Player(player_name, room['outside'], [items['backpack']])
play = True

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def room_greeting():
    print(f"You are in the {player.room.name}.")
    print(f"{player.room.description}")
    if len(player.room.items) == 0:
        room_items = []
        print(f"The room is empty.")
    else:
        room_items = [x.name for x in player.room.items]
        print(f"You see {room_items} in the room.")
    if len(player.inventory) == 0:
        print(f"You have nothing in inventory.\n")
    else:
        player_inventory = [x.name for x in player.inventory]
        print(
            f"You have the following in your inventory: {player_inventory}\n")


print('\n' * 80)
print(f"Welcome to Chad's Game of Awesomeness {player.name}.")
time.sleep(2)
while (play == True):
    room_greeting()
    player_input = input(
        "Please choose a direction by typing 'n', 'e', 's', 'w' or 'q' to quit.\nYou may also type 'l' to look at the items in the room or 't' to take an item or 'd' to drop an item from inventory.")
    if player_input == 'q':
        print(
            f"Thank you for playing Chad's Game of Awesomeness {player.name}.\n")
        play = False
    else:
        if player_input == 'n' or player_input == 'e' or player_input == 's' or player_input == 'w':
            next_room = getattr(player.room, f"{player_input}_to")
            if next_room == 'wall':
                print(
                    f"You've run into a wall! Now wipe the blood from your nose and try a different direction.\n")
            else:
                player.room = next_room
        elif player_input == 'l' or player_input == 't':
            if len(player.room.items) == 0:
                print(f"There are no items in this room.\n")
                time.sleep(2)
            else:
                if player_input == 'l':
                    item_description = [
                        x.description for x in player.room.items]
                    print(f"You see {item_description}\n.")
                    time.sleep(2)
                else:
                    exit = False
                    while exit == False:
                        room_items = [x.short_name for x in player.room.items]
                        print(f"You can take {room_items}")
                        player_input = input("Which item do you want to take?")
                        for i in player.room.items:
                            if player_input == i.short_name:
                                player.inventory.append(i)
                                player.room.items.remove(i)
                                exit = True
                            else:
                                mistake = input(
                                    f"You did not chose a valid item. Do you want to try again? Enter 'y' for yes or 'n' for no.")
                                if mistake == 'n':
                                    exit = True
        elif player_input == 'd':
            if len(player.inventory) == 0:
                print(f"You do not have any inventory to drop.")
            else:
                exit = False
                while exit == False:
                    player_inventory = [x.short_name for x in player.inventory]
                    print(f"You can drop {player_inventory}.")
                    player_input = input("Which item do you want to drop?")
                    for i in player.inventory:
                        if player_input == i.short_name:
                            player.inventory.remove(i)
                            player.room.items.append(i)
                            exit = True
                        else:
                            mistake = input(
                                f"You did not chose a valid item. Do you want to try again? Enter 'y' for yes or 'n' for no.")
                            if mistake == 'n':
                                exit = True
        else:
            print(f"Please enter a valid input.")
