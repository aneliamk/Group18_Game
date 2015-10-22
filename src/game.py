# Group 18 CM1101 Final Game

from map import rooms
from player import *
from items import *
from gameparser import *
from colorama import Fore, Back, Style
from trigger import *
from map_display import *

#returns a comma seperated list of items
def list_of_items(items):
    s = ''
    for index, item in enumerate(items):
        s += item['name']
        if index != len(items)-1:
            s += ', '
    return s
    

#prints a list of items in current room
def print_room_items(room):
    if len(room["items"])>0:
        print ("There is " + list_of_items(room["items"]) + " here.\n")


#prints players inventory
def print_inventory_items(items):
    if len(items)>0:
        print ("You have " + list_of_items(items) + ".")
        print ("")


#prints players stats
def print_player_attributes(health, alcohol_bar, player_money):
    print ("You have " + Fore.GREEN + str(health) + Style.RESET_ALL + " health.")
    print ("You have " + Fore.YELLOW + str(player_money) + Style.RESET_ALL + " pounds. ")
    print ("You have " + Fore.RED + str(victory_points) + Style.RESET_ALL + " victory points. ")
    print ("")


#prints room title, description and list of items
def print_room(room):
    # Display room name
    print("\n")
    print ("*" * 80 + "\n")
    print(Back.WHITE + Fore.BLACK + " " + room["name"].upper() + " " + Style.RESET_ALL)
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)


#returns the name of room in which a particular direction leads
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


#prints the directions that players have available to them
def print_exit(direction, leads_to):
    print(Fore.GREEN + "GO " + direction.upper() + " to " + leads_to + "." + Style.RESET_ALL)


#prints all available commands that player can type
def print_menu(exits, room_items, inv_items):
    print(Style.BRIGHT + "You can:" + Style.RESET_ALL)
    for direction in exits:
        #print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    #prints the items available to take and drop 
    for item in room_items:
        if item["health"] != 0:
            print(Fore.RED + "BUY " + item["id"].upper() + " to take " + item["name"] + "." + Style.RESET_ALL)
        else:
            print(Fore.RED + "TAKE " + item["id"].upper() + " to take " + item["name"] + "." + Style.RESET_ALL)
    for item in inv_items:
        print (Fore.YELLOW + "DROP " + item["id"].upper() + " to drop your " + item["name"] + "." + Style.RESET_ALL) 
    print(Style.BRIGHT + "What do you want to do?" + Style.RESET_ALL)


#returns Boolean as to whether exit is valid
def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


#checks that player has enough money to enter club and then changes points and money 
def enter_club(room):
    global player_money
    global victory_points
    enter = True
    if room["cost"] <= player_money:
        player_money = player_money-room["cost"]
        enter = True
        if "victory_points" in room:
            victory_points = victory_points + room["victory_points"]
    else:
        print("too little cash")
        enter = False
    return enter


#moves player to new room providing the direction is valid
def execute_go(direction):
    global current_room
    global rooms

    exits = current_room["exits"]

    if is_valid_exit(exits, direction) and enter_club(rooms[exits[direction]]):
        if rooms[exits[direction]]["special"] != "":
            key = riddle(rooms[exits[direction]])
            if key == 1:
                current_room = rooms[exits[direction]]
            elif key == 2:
                return
        elif rooms[exits[direction]]["special"] == "":
            current_room = rooms[exits[direction]]
        print("\n" + Back.WHITE + Fore.BLACK + " " + current_room["name"].upper() + " " + Style.RESET_ALL)
    else:
        print("You cannot go there.")


#allows users to pick up items from room and buy consumables such as drinks and food
def execute_take(item_id):
    global current_room
    global max_mass

    ok = False
    items = current_room["items"]

    for item in items:
        if item["id"] == item_id:
            item_name = item["name"]
            if item["health"] != 0:
                global health
                global alcohol_bar
                global player_money
                global victory_points
                if (player_money - item["price"]) >= 0:
                    ok = True
                    health += item ["health"]
                    player_money -= item["price"]
                    victory_points += item["points"]
                    print("You buy " + item["name"])
                    if health > 100:
                        health = 100
                else:
                    print("You don't have enough money to buy that.")
            else:
                ok = True
                if (get_inventory_mass() + item["mass"]) <= max_mass:
                   items.remove(item)
                   inventory.append(item)
                   print("You take " + item["name"])
                else:
                    print("You are over-encumbered, you will need to drop an item")

    if (ok == False):
        print("You cannot take that.")
    else:
        pass
    

#allows player to drop items, moving item from player inventory into room items
def execute_drop(item_id):
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
    

#takes user input and determins what they want to execute
def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go" or command[0] == "move" or command[0] == "walk":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take" or command[0] == "buy":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "map":
        map_creation()

    else:
        print("This makes no sense.")


#changes current room or items in inventory depending on the trigger event
def trigger_trigger(val):
    global health
    global current_room
    global alcohol_bar    
    global inventory
    global triggers
    val["exe"] = "yes"
    health = health + val["health effect"]
    if val["room_change"] != "":
       current_room = rooms[val["room_change"]]
    print(val["description"])
    if val["item_add"] != "":
        inventory.append(val["item_add"])
    input()


#checks if room has trigger event
def check_trigger():
    for val in triggers:
        if (("health" == triggers[val]["health"] or triggers[val]["health"] == -1) and (current_room["name"] == triggers[val]["room"] or triggers[val]["room"] == "any") and (triggers[val]["item"] in inventory or triggers[val]["item"] == "") and (triggers[val]["exe"] == "no")):
           trigger_trigger(triggers[val])


#prints information and takes input from user
def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)

    user_input = input(Fore.MAGENTA + "> " + Style.RESET_ALL)

    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


#returns Boolean if user chooses to move towards exit with the name given by direction
def move(exits, direction):
    return rooms[exits[direction]]


#checks if user has won or lost the game in current state
def check_victory():
    if victory_points >= 8 and current_room == rooms["Your room"] and item_keys in inventory:
        win()
    elif health <= 0:
        print("""Your health has reached zero!!! 
You are unresponsive and have slipped into a state on unconsciousness.""")
        lose()        
    elif current_room == rooms["Your room"] and ((item_keys not in inventory) and (item_keys not in rooms["Your room"]["items"])): 
        print("""You had a great night out full of adventure and (mostly) drunkness. BUT WAIT YOU DONT HAVE YOUR KEYS, you sleep on the cold hard ground, what a sad way to end your night.""")
        lose()
    elif current_room == rooms["Police"]:
        print(Back.WHITE + Fore.BLACK + " POLICE STATION " + Style.RESET_ALL + "\n")
        print(rooms["Police"]["description"])
        lose()
    elif current_room == rooms["KFC"]:
        # Display room name
        print("\n" * 3)
        print ("*" * 80 + "\n")
        print(Back.WHITE + Fore.BLACK + " " + rooms["KFC"]["name"].upper() + " " + Style.RESET_ALL)
        print()
        # Display room description
        print(rooms["KFC"]["description"])
        print()
        lose()
    else:
        pass


#initialises end of game and prints 'YOU LOSE'
def lose():
    print(" __     ______  _    _   _      ____   _____ ______") 
    print(" \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|")
    print("  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   ")
    print("   \   /| |  | | |  | | | |   | |  | |\___ \|  __|  ")
    print("    | | | |__| | |__| | | |___| |__| |____) | |____ ")
    print("    |_|  \____/ \____/  |______\____/|_____/|______|")
    print(" ")
    return end_game()


#initialises end of game and prints 'YOU WIN'
def win():
    print("""Congratulations! You went out into Cardiff, had a great night, 
drank lots but not too much and returned home safely! Make sure 
you have a big glass of water so you feel fresh in the morning 
ready for your 9am lecture.""")
    print(" __     ______  _    _  __          _______ _   _ ")
    print(" \ \   / / __ \| |  | | \ \        / /_   _| \ | |")
    print("  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |")
    print("   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |")
    print("    | | | |__| | |__| |    \  /\  /   _| |_| |\  |")
    print("    |_|  \____/ \____/      \/  \/   |_____|_| \_|")
    return end_game()


#resets all player stats, room items, player inventory and trigger exe
def end_game():
    input("Press Enter to restart game... ")
    print("\n" * 40)
    global current_room
    global inventory
    current_room = rooms["Halls"]
    inventory = [item_keys, item_phone, item_id]
    current_room["inventory"] = []
    global health 
    health = 100
    global player_money 
    player_money = 50
    global max_mass
    max_mass = 4
    global victory_points 
    global rooms
    victory_points = 0
    rooms["Halls"]["items"] = []
    rooms["Your room"]["items"] = []
    rooms["Mama Kebab"]["items"] = [item_thick_sausage_kebab, item_long_sausage_kebab]
    rooms["Outside SU"]["items"] = []
    rooms["SU Tills"]["items"] = []
    rooms["SU Dancefloor"]["items"] = [unknown_substance]
    rooms["SU Bar"]["items"] = [item_sambuca_shot, item_tequila_shot, item_vodka, item_jagerbomb_shot, item_water]
    rooms["Tiger Tiger"]["items"] = []
    rooms["Tiger Tiger Tills"]["items"] = []
    rooms["Upstairs Live Lounge"]["items"] =[item_sambuca_shot, item_jagerbomb_shot, item_vodka, item_jack_daniels, item_water]
    rooms["Tiger Tiger - The Groovy Wonderland"]["items"] = []
    rooms["Tiger Tiger - The Club"]["items"] = [item_sambuca_shot, item_jagerbomb_shot, item_vodka, item_jack_daniels, item_water]
    rooms["Live Lounge"]["items"] = []
    rooms["Live Lounge Bar"]["items"] = []
    rooms["Glam"]["items"] = []
    rooms["Glam Tills"]["items"] = []
    rooms["Glam Bar"]["items"] = [item_WKD, item_vodka, item_desperados, item_jack_daniels, item_water]
    rooms["Pryzm Entrance"]["items"] = []
    rooms["Pryzm"]["items"] = []
    rooms["Pryzm Tills"]["items"] = []
    rooms["Pryzm Disco"]["items"] = [item_WKD, item_vodka, item_sambuca_shot, item_jack_daniels, item_water]
    rooms["Pryzm Curve"]["items"] = [item_WKD, item_vodka, item_sambuca_shot, item_jack_daniels, item_water]
    rooms["Pryzm House"]["items"] = [item_stella, item_coors, item_crabbies, item_budweiser, item_bulmers, item_jagerbomb_shot, item_sambuca_shot, item_jack_daniels, item_water]
    rooms["McDonalds"]["items"] = [item_nuggets, item_big_mac, item_mcflurry, item_happy_meal]
    rooms["Cab"]["items"] = []
    for val in triggers:
        triggers[val]["exe"] = "no"


#prints riddle and checks if user input is correct
def riddle(val):
    check = False  
    while check == False:
          print(val["special"])
          x = input("What is the answer? ")
          x = x.lower()
          if val["answer"] == x:
              check = True
              print("Correct - you are allowed in.")
              key = 1
              return key
          elif x == "back":
               check = True
               print("ok")
               key = 2
               return key
          else:
              print("That is wrong!")
              input("Press enter to try again...") 


# This is the entry point of our program
def main():
    print("\n" * 50)
    print("""Welcome to 'Drink But Don't Drop'. 
The aim is to visit the bars and clubs in Cardiff and have a 
great night, returning to your room in Halls safe and sound. 
But be careful - if you go anywhere you shouldn't, get too 
drunk, return to your room too early or get into trouble with 
the law then you will lose the game. Think about each move 
you make and you will be sure to succeed.

Type your commands when prompted. Type 'map' at any time to
display a map of the game.

ENJOY!\n""")

    input("Press enter to continue... ")
    print ("\n" * 50)
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        print_player_attributes(health, victory_points, player_money)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)
        check_trigger()
        check_victory()



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

