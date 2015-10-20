from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

health = 100

alcohol_bar = 35

player_money = 50

max_mass = 4

# Start game at the uni halls
current_room = rooms["Halls"]

def get_inventory_mass():
    TotalMass = 0.0
    for item in inventory:
        TotalMass += item["mass"]
    return TotalMass