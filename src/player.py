#author Viktor and Jake

from items import *
from map import rooms

inventory = [item_keys, item_phone, item_id]

health = 100

player_money = 50

max_mass = 4

victory_points = 0

# Start game at the uni halls
current_room = rooms["Halls"]

def get_inventory_mass():
    TotalMass = 0.0
    for item in inventory:
        TotalMass += item["mass"]
    return TotalMass