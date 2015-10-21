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

Fight = {"drink": -1,

"health": -1,

"health effect": -20,

"drink effect": 0,

"room": "Mama Kebab" ,

"room_change": "",

"item": "",

"item_change": "",

"item_add": "",

"description": 

  """ You are attacked by a crazy man. You weave and dodge with elegance and speed. You would have been fine if it wasen't for the fact you got knocked out cold""",

}



Wallet = {"drink": -1,

"health": -1,

"health effect": -5,

"drink effect": 0,

"room": "SU Dancefloor" ,

"room_change": "",

"item": "",

"item_change": "" ,

"item_add": Unknown_substance,

"description": 

  """ a large bag of unknown substace you find in a wallet you do.""",

}



coca = {"drink": -1,

"health": -1,

"health effect": 0,

"drink effect": 0,

"room": "McDonalds" ,

"room_change": "Police",

"item": Unknown_substance,
"item_add": "",

"item_change": "",

"description": 

  """ Police search you as part of a random sweep. Good news you now know what the white stuff was. Bad news it was cocain. """,}



triggers = { 

"disco": Disco,

"binary": Binary_Drink,

"fight": Fight,

"wallet": Wallet,
"coca": coca,

 

 }







