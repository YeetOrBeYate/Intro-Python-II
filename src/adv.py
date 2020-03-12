from room import Room
from player import Player
from item import Item, Food, Tool

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

#creating the default items
item = {
    'Cheese': Food('Cheddar', 'Slightly stale but tasty cheese block', 300),
    'Orb' : Item('Ender Orb', 'minecraft thing'),

    'waste': Item('Dust', 'some kind of powdering substance..maybe'),

    'other': Item('Yeet', 'This is that good stuff'),

    'Pick': Tool('Iron PickAxe', 'Used to mine', 4.5)
}


#adding defualt items to rooms

room['outside'].set_items(item['Pick'])
room['foyer'].set_items(item['Orb'])
room['overlook'].set_items(item['Cheese'])
room['narrow'].set_items(item['waste'])
room['treasure'].set_items(item['other'])
room['treasure'].set_items(item['other'])



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

name = str(input("Please type your name "))

player = Player(name, room['outside'])

player.print_info()

valid_directions = ('n', 's', 'e', 'w')

item_commands = ('grab', 'drop')

while True:

    cmd = str(input("~~> "))

    if cmd in valid_directions:
        player.travel(cmd)
        
    elif cmd == 'q':
        print("Goodbye!")
        exit(0)  
    elif cmd in item_commands:
        player.grab_item(cmd)
    else:
        print('dont understand command')
          
    




#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
