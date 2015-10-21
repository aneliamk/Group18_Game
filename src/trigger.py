# -*- coding: utf-8 -*-

"""

Created on Mon Oct 19 11:21:22 2015



@author: c1525969

"""

from items import *

Disco = {"drink": -1,

"health": -1,

"health effect": 0,

"drink effect": 0,

"room": "Tiger Tiger - The Groovy Wonderland",

"room_change": "Police",

"item": "",

"item_add": "",

"description": "To prison criminal scum" ,

}



Binary_Drink = {"drink": -1,

"health": -1,

"health effect": -100000,

"drink effect": 0,

"room": "Live Lounge",

"room_change": "",

"item": "",

"item change": "",

"item_add": "",

"description": 

  """  - 001 shot down.\n

    - 010 shots down.\n

    - 011 and you begin to regret this decision but it’s too late to leave now.\n

    - 100 shots.\n

    - 101.\n

    - 111.........and spew. You projectile vomit across the bar.\n

    Matt and Kirill continue drinking laughing at your feeble attempt to keep

    up with them.?\n

    """,

}

Fight = {

"drink": -1,

"health": -1,

"health effect": -20,

"drink effect": 0,

"room": "Mama Kebab" ,

"room_change": "",

"item": "",

"item_change": "",

"item_add": "",

"description": 
"""
You are attacked by a drunken thug standing outside Mamas. 
You weave and dodge with elegance and speed despite your drunkenness. 
You escape with only minor injuries. 
Maybe you should avoid Mamas from now on.

Press Enter to continue...""",

}



Wallet = {"drink": -1,

"health": -1,

"health effect": -5,

"drink effect": 0,

"room": "SU Dancefloor" ,

"room_change": "",

"item": "",

"item_change": "" ,

"item_add": unknown_substance,

"description": 

"""You find a bag of an unknown substance on the floor you pick it up. 
Could this be the stuff to make your night?

Press Enter to continue...""",

}



coca = {"drink": -1,

"health": -1,

"health effect": 0,

"drink effect": 0,

"room": "McDonalds" ,

"room_change": "Police",

"item": unknown_substance,
"item_add": "",

"item_change": "",

"description": 

"""The bright lights of McDonalds reveal what you really look like after 
a night out. You begin attracting attention as you stumble around trying 
to hold yourself together. 

A police officer walks in and immedietly takes an interest in you. He 
walks over and decides to search you for anything illegal. 

He discovers the substance you found in the Student's Union and slaps 
the cuffs on you. You are carried away, head hanging gwith shame. """,}



triggers = { 

"disco": Disco,

"binary": Binary_Drink,

"fight": Fight,

"wallet": Wallet,
"coca": coca,

 

 }







