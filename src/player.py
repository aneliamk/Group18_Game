from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

health = 50

alcohol_bar = 35


max_mass = 3.0
# Start game at the uni halls
current_room = rooms["Halls"]

def get_inventory_mass():
    TotalMass = 0.0
    for item in inventory:
        TotalMass += item["mass"]
    return TotalMass