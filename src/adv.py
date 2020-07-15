from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("Please enter your name: ")
player = Player(player_name, room['outside'])
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

print('\n' * 80)
print(f"Welcome to Chad's Game of Awesomeness {player.name}.")
time.sleep(2)
while (play == True):
    print(f"You are in the {player.room.name}.")
    print(f"{player.room.description}\n")

    player_input = input(
        "Please choose a direction by typing n, e, s, w or q to quit.")
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
        else:
            print(f"Please enter a valid input.")
