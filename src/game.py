#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from colorama import Fore, Back, Style

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    s = ''
    for index, item in enumerate(items):
        s += item['name']
        if index != len(items)-1:
            s += ', '
    return s
    

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if len(room["items"])>0:
        print ("There is " + list_of_items(room["items"]) + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    if len(items)>0:
        print ("You have " + list_of_items(items) + ".")
        print ("")

def print_player_attributes(health, alcohol_bar, player_money):
    print ("You have " + Fore.GREEN + str(health) + Style.RESET_ALL + " health.")
    print ("You have " + Fore.RED + str(alcohol_bar) + Style.RESET_ALL + " percent alcohol in your system. ")
    print ("You have " + Fore.YELLOW + str(player_money) + Style.RESET_ALL + " pounds. ")
    print ("")

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print("\n" * 40)
    print ("*" * 80 + "\n")
    print(Back.WHITE + Fore.BLACK + " " + room["name"].upper() + " " + Style.RESET_ALL)
    print()
    # Display room description
    print(room["description"])
    #.encode("utf-8") AFTER DESCRIPTION IF IT DOESN'T WORK ON OTHER COMPUTER
    print()

    #
    #if len(room["items"]) > 0:
    print_room_items(room)
    #

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print(Fore.GREEN + "GO " + direction.upper() + " to " + leads_to + "." + Style.RESET_ALL)


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print(Style.BRIGHT + "You can:" + Style.RESET_ALL)
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print (Fore.RED + "TAKE " + item["id"].upper() + " to take " + item["name"] + "." + Style.RESET_ALL)

    for item in inv_items:
        print (Fore.YELLOW + "DROP " + item["id"].upper() + " to drop your " + item["name"] + "." + Style.RESET_ALL)

    #
    
    print(Style.BRIGHT + "What do you want to do?" + Style.RESET_ALL)


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    global rooms
    exits = current_room["exits"]
    if is_valid_exit(exits, direction):
        current_room = rooms[exits[direction]]
        print(current_room["name"])
    else:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    global max_mass

    ok = False
    for item in current_room["items"]:
        if item["id"] == item_id:
            if item["health"] != 0 or item["alcohol_bar"] != 0:
                global health
                global alcohol_bar
                global player_money
                if (player_money - item["price"]) >= 0:
                    health += item["health"]
                    alcohol_bar += item["alcohol_bar"]
                    player_money -= item["price"]
                    ok = True          
                elif (get_inventory_mass() + item["mass"]) <= max_mass:
                   current_room["items"].remove(item)
                   inventory.append(item)
                elif (get_inventory_mass() + item["mass"]) > max_mass:
                    print("You are over-encumbered, you will need to drop an item")
                else:
                    print("You don't have enough money to buy that.")
                    return
            elif (get_inventory_mass() + item["mass"]) <= max_mass:
                current_room["items"].remove(item)
                inventory.append(item)
                ok = True
            taken_item = item["name"]
    if (ok == False):
        print("You cannot take that.")
    else:
        print("You take " + taken_item)
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    ok = False

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            ok = True
        else:
            pass
    if (ok == False):
        print("You cannot drop that.")
    else:
        pass
    return
    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input(Fore.MAGENTA + "> " + Style.RESET_ALL)

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


"""def check_victory():
    if player["victory_points"] <= 8 and current_room == rooms["Halls"] and "keys" in inventory:
        win()
    elif player["health"] <= 0:
        lose()        
        print("you have drunck too much and your drunck body is on the floor good luck next time")
    elif player["victory_points"] <= 8 and current_room == rooms["Halls"] and "keys" not in inventory: 
        print("You had a great night out full of adventure and (mostly) drunkness. BUT WAIT YOU DONT HAVE YOUR KEYS, you sleep on the cold hard ground")
        lose()
    elif current_room == rooms("Prison"):
        print("what ever you did it was serious")
        lose()
    elif player["alcohole bar"] >= 100:
        print("to much alcohole")
        lose()
    elif current_room == rooms["KFC"]:
        print("ITS CLOSED YOU DIE OF SHAME")
        lose()"""


def lose(inventory, current_room, player):
    print(" __     ______  _    _   _      ____   _____ ______") 
    print(" \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|")
    print("  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   ")
    print("   \   /| |  | | |  | | | |   | |  | |\___ \|  __|  ")
    print("    | | | |__| | |__| | | |___| |__| |____) | |____ ")
    print("    |_|  \____/ \____/  |______\____/|_____/|______|")
    end_game(inventory,current_room, player)


def win(inventory, current_room, player):
    print(" __     ______  _    _  __          _______ _   _ ")
    print(" \ \   / / __ \| |  | | \ \        / /_   _| \ | |")
    print("  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |")
    print("   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |")
    print("    | | | |__| | |__| |    \  /\  /   _| |_| |\  |")
    print("    |_|  \____/ \____/      \/  \/   |_____|_| \_|")
    end_game(inventory,current_room, player)


def end_game(inventory, current_room, player):
    current_room = rooms["Halls"]
    inventory = [id, laptop, keys]


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        print_player_attributes(health, alcohol_bar, player_money)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)
        #check_victory()



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

