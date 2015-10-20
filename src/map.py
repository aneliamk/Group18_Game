__author__ = 'ioana'

from items import *

#Halls --------------------------------------------------------

room_halls = {
    "name": "Outside University Halls",

    "description":
    """You are standing outside your Halls. 
You can go inside to your room or venture out into Cardiff.""",

    "exits":  {"south": "Pryzm Entrance", "west": "Kebab", "cab": "Cab", "room": "Your room"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": ""
}

#Dorm ---------------------------------------------------------

room_dorm = {
    "name": "Your room",

    "description":
    """The familiar feel of halls. With dirty dishes and empty bottles of vodka 
you are happy to be home. """,

    "exits": {"outside": "Halls"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": ""
}

#Mama Kebab ---------------------------------------------------

room_kebab = {
    "name": "Mama Kebab",

    "description":
    """Good choice. Kfw (Kebab for the win). You have a choice of buying a 
\'Thick Sausage Kebab\' or a \'Long Sausage Kebab\'. Mama is getting impatient,
what are you going to go for?""",

    "exits":  {"west": "SU", "east": "Halls" , "cab": "Cab"},

    "items": [],
    "victory_points": 2,

    "special": "" ,

    "answer": ""
}

#Student Union ------------------------------------------------


room_su = {
    "name": "Outside Student's Union",

    "description":
    """You are standing outside the Students Union, entry costs £5, where do
you want to go?""",

    "exits":  {"south": "Live Lounge", "east": "Kebab", "cab": "Cab", 
    #"inside": "Student's Union"
    "dancefloor": "SU Dancefloor",
    "bar": "SU Bar"
    },

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}

room_su_dancefloor = {
    "name": "Student's Union Dancefloor",

    "description":
    """The cheap drinks have drawn you in. You look around Y Plas
and see a wallet on the floor. The bar is busy but well staffed and drinks
here are cheaper than elsewhere. What do you do next?""",

    "exits":  {#"south": "Live Lounge", "east": "Mama Kebab", "cab": "Cab",
    "outside": "SU",
    "bar": "SU Bar"
    },

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}

room_su_bar = {
    "name": "Student's Union Bar",

    "description":
    """CUSU Menu:
Sambuca - £1
Tequila - £1
Vodka - £1
Jagerbomb - £2
Water - Free
The young bar man looks at you, “What do you want Fresher?” """,

    "exits":  {#"south": "Live Lounge", "east": "Mama Kebab", "cab": "Cab"
    "outside": "SU",
    "dancefloor": "SU Dancefloor"
    },

    "items": [item_sambuca_shot, item_tequila_shot, item_vodka, item_jagerbomb_shot, item_water], #need to add dictionary of drinks i think, not sure about how the menu will print also.
    
    "victory_points": 2,

    "special": "",

    "answer": ""
}

#-------------------------------------------------------
#This will be an event
"""
room_su_wallet = {
    "name": "Student's Union",

    "description":
    You pick up the wallet and find that there is no money in it. But what did you
    expect? You’re in the SU full of very broke students! You do however find an expired
    condom still in its foil wrapper. You keep the condom as a precaution and toss the
    wallet back on the floor continuing with your night.,

    "exits":  {"south": "Live Lounge", "east": "Kebab", "cab": "Cab"},

    "items": ['Expired Condom']
}
"""

#Tiger Tiger --------------------------------------------

room_tiger = {
    "name": "Tiger Tiger - The entrance",

    "description":
    """Entering Tiger Tiger you have two choices. Go to the ‘Groovy Wonderland’ or
'The Club’.""",

    "exits":  {"south": "McDonalds",
               "east":"Glam",
               "west":"Live Lounge",
               "cab": "Cab",
               "wonder": "Tiger Wonder",
               "club": "Tiger Club"
               },

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}


room_tiger_wonder = {
    "name": "Tiger Tiger - The Groovy Wonderland",

    "description":
    """Really? 80s Disco anthems? You have no choice to crack out some killer 
moves but people don’t seem impressed. After a while a police officer approaches. 
“Excuse me sir”, he interrupts you mid hip thrust, “We have had reports of 
criminal dance moves in this establishment tonight”. A wave of embarrassment 
rushes over you, you knew you shouldn’t have gone for the moon walk. He slaps
the cuffs around your wrists and takes you to the police station.""",

    "exits":  { "wonder": "Tiger Wonder", "entrance": "Tiger Tiger"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}


room_tiger_club = {
    "name": "Tiger Tiger - The Club",

    "description":
    """You enter ‘The Club’ and your initial survey suggest that the Tiger Tiger 
management do indeed know what a club is. You notice a bag containing a mysterious
substance on the floor. You can pick up the package or leave it.""",

    "exits": {"club": "Tiger Club", "entrance": "Tiger Tiger"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}

# Live Lounge -------------------------------------------------

room_lounge = {
    "name": "Live Lounge",

    "description":
    """Free entry here, it's your lucky day! As soon as you approach the bar, you see 
Kirill and Matt doing Russian Standard shots counting in binary. Do you run? Or join 
them?""",

    "exits":  {"north": "SU", "east": "Tiger Tiger", "cab": "Cab"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}

#--------------------------------------------------------------
#MIGHT NOT BE GOOD---------------------------------------------
"""
room_lounge_bar = {
    "name": "Live Lounge",

    "description":
    - 001 shot down.\n
    - 010 shots down.\n
    - 011 and you begin to regret this decision but it’s too late to leave now.\n
    - 100 shots.\n
    - 101.\n
    - 111.........and spew. You projectile vomit across the bar.\n
    Matt and Kirill continue drinking laughing at your feeble attempt to keep
    up with them.?\n
    - GAME OVER!,

    "exits":  {},

    "items": []
    "victory_points": 2
}

room_lounge_hide = {
    "name": "Live Lounge",

    "description":
    You move to the other side of the floor away from the two doctors. A wise move, they
    are doing more shots than you could ever handle. What would you like to do next?,

    "exits":  {"north": "SU", "east": "Tiger Tiger", "cab": "Cab"},

    "items": []
    "victory_points": 2
}

"""

# Glam ---------------------------------------------------------

room_glam = {
    "name": "Glam",

    "description":
    """Standing at the entrance to Glam you notice the bouncers here are 
particularly tough. They stand legs shoulder width apart scanning the queue for 
potential trouble makers.""",

    "exits":  {"south": "McDonalds", "east":"Pryzm Entrance", "west":"Tiger Tiger", "cab":"Cab", "inside": "Glam Bar"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}

room_glam_bar = {
    "name": "Glam Bar",

    "description":
    """Good ol’ Glam. Some love it, some hate it. You decided to come here so 
complain. You head straight for the bar and look at the menu.\n
Glam Menu:
WKD - £3
Vodka - £2
Desperados - £3
Jack Daniels - £3
Water - Free""",

    "exits": {"outside": "Glam"},

    "items": [item_WKD, item_vodka, item_desperados, item_jack_daniels, item_water],

    "special": "" ,

    "answer": ""
}

# Pryzm -------------------------------------------------
room_pryzm_entrance = {
    "name": "Pryzm Entrance",

    "description":
    """Long queues greet you at the Pryzm Entrance and you debate whether or not 
it is really a good idea to wait or whether you shoud go somewhere quieter. The 
choice is yours.""",

    "exits":  {"north": "Halls",
               "south": "McDonalds",
               "east": "KFC",
               "west": "Glam",
               "cab": "Cab",
               "inside": "Pryzm"
               },

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}


room_pryzm = {
    "name": "Pryzm",

    "description":
    """Ahh Pryzm, the staple club of any freshers night out. With a choice of 
music and a variety of bars to choose from you feel content with your choice of 
club and feel that the long wait outside with the ever annoying Paper reps was 
probably worth it. You have a choice of the House, Curve or Disco room, or you 
can head back outside.""",

    "exits":  {"outside": "Pryzm Entrance",
               "curve": "Pryzm Curve",
               "house": "Pryzm House",
               "disco": "Pryzm Disco",
               },

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}


room_pryzm_disco = {
    "name": "Pryzm - The Disco area",

    "description":
    """Great choice. Only here can you do the Macarena and YMCA and not look like a 
total d*ck. Your mighty fine hips attract a plethora of female attention and before 
you know it you’ve pulled. Great work.""",

    "exits":  {"entrance": "Pryzm Entrance", "curve": "Pryzm Curve", "house": "Pryzm House"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}


room_pryzm_curve = {
    "name": "Pryzm - Curve area",

    "description":
    """Interesting choice. Many do not even know this room exists. You are rewarded 
with good music, a quiet(ish) bar and not being surrounded by \'Cheeky Archbishop of 
Banterbury Top Lads\' that you usually find in Pryzm.""",

    "exits":  {"entrance": "Pryzm Entrance", "house": "Pryzm House", "disco": "Pryzm Disco"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}


room_pryzm_house = {
    "name": "Pryzm - House area",

    "description":
    """We’re not actually sure about the name of this room but it’s pretty busy and 
the strobe lighting probably isn\'t good for your epilepsy. You feel your health 
declining""",

    "exits":  {"entrance": "Pryzm Entrance", "curve": "Pryzm Curve", "disco": "Pryzm Disco"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
}

#McDonalds ----------------------------------------------------

room_mc = {
    "name": "McDonalds",

    "description":
    """Fair, you wanted to find somewhere close and cheap but now you have to eat 
shit served in paper containers.\n
McMenu:
9 McNuggets - £5
Big Mac - £5
McFlurry - £1
Happy Meal - £5\n
“Can I help you?”, the voice of the worker behind the counter screams at you.""",

    "exits":  {"north": "Glam", "east":"Pryzm Entrance", "west":"Tiger Tiger", "cab":"Cab"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": ""
} #need to add the 'would you like fries with that', im not sure how.

#KFC ----------------------------------------------------------

room_kfc = {
    "name": "KFC",

    "description":
    """You arrive to the locked doors of KFC, tears dripping down your face you 
collapse into a heap on the floor. You should have known that KFC closes at 11:00pm 
but you didn’t think it through. How can you continue with your night after this 
great ordeal?!\n
-----\n""",

    "exits":  {},
    
    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": ""

}


#Police Station ---------------------------------------------

room_police = {
    "name": "Police Station",

    "description":
    """Bright lights blind you as PC Bacon unlocks your handcuffs and hands your 
over to Detective Lou Tennant, they look at you like you’re a piece of chewing gum 
stuck to the sole of a shoe. With great pleasure he throws you into the overnight 
cell and locks the door. \n
----- \n""",

    "exits":  {},

    "items": [],

    "special": "",

    "answer": ""
}

#Cab---------------------------------------------------------

room_cab = {
    "name": "Dragon Taxis",

    "description":
    """You get in the taxi and the aroma of faux leather overwhelms your senses. 
Taxi driver with the ID reading \'Justin Sider\' turns to you and asks where you
would like to go?.""",

    "exits": {"pryzm": "Pryzm Entrance",
              "glam": "Glam",
              "tiger": "Tiger Tiger",
              "lounge": "Live Lounge",
              "su": "SU",
              "kebab": "Kebab",
              "halls": "Halls",
              "kfc": "KFC"},

    "items": [],

    "special": "",

    "answer": ""
}


rooms = {
    "Your room": room_dorm,
    "Halls": room_halls,
    "Kebab": room_kebab,

    "SU": room_su,
    "SU Bar": room_su_bar,
    "SU Dancefloor": room_su_dancefloor,

    "Live Lounge": room_lounge,
    #"Live Lounge Bar": room_lounge_bar,

    "Tiger Tiger": room_tiger,
    "Tiger Wonder": room_tiger_wonder,
    "Tiger Club": room_tiger_club,

    "Glam": room_glam,
    "Glam Bar": room_glam_bar,

    "Pryzm Entrance": room_pryzm_entrance,
    "Pryzm": room_pryzm,
    "Pryzm Disco": room_pryzm_disco,
    "Pryzm Curve": room_pryzm_curve,
    "Pryzm House": room_pryzm_house,

    "McDonalds": room_mc,

    "KFC": room_kfc,

    "Police": room_police,
    
    "Cab": room_cab

}



