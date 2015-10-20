__author__ = 'ioana'

from items import *

#Halls --------------------------------------------------------

room_halls = {
    "name": "Outside University Halls",

    "description":
    """  """,

    "exits":  {"south": "Pryzm", "west": "Kebab", "cab": "Cab", "room": "Your room"},

    "items": [item_tequila_shot, item_biscuits, item_pen],

    "points": 2
}

#Dorm ---------------------------------------------------------

room_dorm = {
    "name": "Your dorm",

    "description":
    """ """,

    #when you return here and enter the room, you win

    "exits": {"outside": "Halls"},

    "items": [],
    "points": 2
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
    "points": 2
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
    "points": 2
}

room_su_dancefloor = {
    "name": "Student's Union Dancefloor",

    "description":
    """The cheap drinks and young girls have drawn you in. You look around Y Plas
    and see a wallet on the floor. The bar is busy but well staffed and drinks
    here are cheaper than elsewhere. What do you do next?""",

    "exits":  {#"south": "Live Lounge", "east": "Mama Kebab", "cab": "Cab",
    "outside": "SU",
    "bar": "SU Bar"
    },

    "items": [],
    "points": 2
}

room_su_bar = {
    "name": "Student's Union Bar",

    "description":
    """CUSU Menu:\n
       Sambuca - £1\n
       Tequila - £1\n
       Vodka - £1\n
       Jagerbomb - £2\n
       Water - Free\n
       The young bar man looks at you, “What do you want Fresher?” """,

    "exits":  {#"south": "Live Lounge", "east": "Mama Kebab", "cab": "Cab"
    "outside": "SU",
    "dacefloor": "SU Dancefloor"
    },

    "items": [],#need to add dictionary of drinks i think, not sure about how the menu will print also.
    "points": 2
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
    """Entering Tiger Tiger you have two choices. Go to the ‘Groovy Wonderland’ or ‘The Club’.""",

    "exits":  {"south": "McDonalds",
               "east":"Glam",
               "west":"Live Lounge",
               "cab": "Cab",
               "wonder": "Tiger Wonder",
               "club": "Tiger Club"
               },

    "items": [],
    "points": 2
}


room_tiger_wonder = {
    "name": "Tiger Tiger - The Groovy Wonderland",

    "description":
    """Really? 80s Disco anthems? You have no choice to crack out some killer moves but people don’t
seem impressed. After a while a police officer approaches. “Excuse me sir”, he interrupts you mid
hip thrust, “We have had reports of criminal dance moves in this establishment tonight”. A wave of
embarrassment rushes over you, you knew you shouldn’t have gone for the moon walk. He slaps
the cuffs around your wrists and takes you to the police station.""",

    "exits":  { "wonder": "Tiger Wonder", "entrance": "Tiger Tiger"},

    "items": [],
    "points": 2
}


room_tiger_club = {
    "name": "Tiger Tiger - The Club",

    "description":
    """You enter ‘The Club’ and your initial survey suggest that the Tiger Tiger management do indeed
know what a club is. You notice a bundle of glow sticks on the floor and go to pick them up but you
don’t have room to fit them in your pockets, you’ll need to swap either your ID, Phone or Keys to fit
them in. What are you going to choose?""",

    "exits":  {"club": "Tiger Club", "entrance": "Tiger Tiger"},

    "items": [],
    "points": 2
}

# Live Lounge -------------------------------------------------

room_lounge = {
    "name": "Live Lounge",

    "description":
    """As soon as you approach the bar, you see Kirill and Matt doing Russian Standard shots
    counting in binary. Do you run? Or join them?""",

    "exits":  {"north": "SU", "east": "Tiger Tiger", "cab": "Cab"},

    "items": [],
    "points": 2
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
    "points": 2
}

room_lounge_hide = {
    "name": "Live Lounge",

    "description":
    You move to the other side of the floor away from the two doctors. A wise move, they
    are doing more shots than you could ever handle. What would you like to do next?,

    "exits":  {"north": "SU", "east": "Tiger Tiger", "cab": "Cab"},

    "items": []
    "points": 2
}

"""

# Glam ---------------------------------------------------------

room_glam = {
    "name": "Glam",

    "description":
    """   """,

    "exits":  {"south": "McDonalds", "east":"Pryzm", "west":"Tiger Tiger", "cab":"Cab", "inside": "Glam Bar"},

    "items": [],
    "points": 2
}

room_glam_bar = {
    "name": "Glam Bar",

    "description":
    """Good ol’ Glam. Some love it, some hate it. You decided to come here so don’t complain. You head
straight for the bar and look at the menu.""",

    "exits": {"outside": "Glam"},

    "items": []
}

# Pryzm -------------------------------------------------

room_pryzm = {
    "name": "Pryzm - The entrance",

    "description":
    """Ahh Pryzm, the staple club of any freshers night out. With a choice of music and a variety of bars
to choose from you feel content with your choice of club and feel that the long wait outside with the
ever annoying Paper reps was probably worth it.""",

    "exits":  {"north": "Halls",
               "south": "McDonalds",
               "east": "KFC",
               "west": "Glam",
               "cab": "Cab",
               "curve": "Pryzm Curve",
               "house": "Pryzm House",
               "disco": "Pryzm Disco",
               },

    "items": [],
    "points": 2
}


room_pryzm_disco = {
    "name": "Pryzm - The Disco area",

    "description":
    """Great choice. Only here can you do the Macarena and YMCA and not look like a total d*ck. Your
mighty fine hips attract a plethora of female attention and before you know it you’ve pulled. Great
work.""",

    "exits":  {"entrance": "Pryzm", "curve": "Pryzm Curve", "house": "Pryzm House"},

    "items": [],
    "points": 2
}


room_pryzm_curve = {
    "name": "Pryzm - Curve area",

    "description":
    """Interesting choice. Many do not even know this room exists. You are rewarded with good music, a
quiet(ish) bar and not being surrounded by \'Cheeky Archbishop of Banterbury Top Lads\' that you
usually find in Pryzm.""",

    "exits":  {"entrance": "Pryzm", "house": "Pryzm House", "disco": "Pryzm Disco"},

    "items": [],
    "points": 2
}


room_pryzm_house = {
    "name": "Pryzm - House area",

    "description":
    """We’re not actually sure about the name of this room but it’s
pretty busy and the strobe lighting probably isn\'t good for
your epilepsy.
-
Nope this really isn’t helping your epilepsy. You collapse to
the floor and the room goes black. GAME OVER.""",

    "exits":  {"entrance": "Pryzm", "curve": "Pryzm Curve", "disco": "Pryzm Disco"},

    "items": [],
    "points": 2
}

#McDonalds ----------------------------------------------------

room_mc = {
    "name": "McDonalds",

    "description":
    """Fair, you wanted to find somewhere close and cheap but now
you have to eat shit served in paper containers.\n
McMenu:\n
9 McNuggets - £5\n
Big Mac - £5\n
McFlurry - £1\n
Happy Meal - £5\n
“Can I help you?”, the voice of the worker behind the counter screams at you.""",

    "exits":  {"north": "Glam", "east":"Pryzm", "west":"Tiger Tiger", "cab":"Cab"},

    "items": [],
    "points": 2
} #need to add the 'would you like fries with that', im not sure how.

#KFC ----------------------------------------------------------

room_kfc = {
    "name": "KFC",

    "description":
    """You arrive to the locked doors of KFC, tears dripping down your
face you collapse into a heap on the floor. You should have
known that KFC closes at 11:00pm but you didn’t think it
through. How can you continue with your night after this great
ordeal?!\n
-----\n
GAME OVER.""",

    "exits":  {},
    
    "items": [],
    "points": 2

}

#Alcohol Detention Centre -----------------------------------

room_detention = {
    "name": "Alcohol Detention Centre",

    "description":
    """Uh-oh. You shouldn’t have had that last drink. You got way too drunk and now you’re in the alcohol
detention centre. They gave you magical medicine, you can now continue your night. Your health
has been restored to 100%, but your fun points have been affected badly. (Return player to outside
Pryzm with health of 100 but -5 points)""",

    "exits":  {"cab":"Cab"},


    "items": [],
    "points": -5
}

#Police Station ---------------------------------------------

room_police = {
    "name": "Police Station",

    "description":
    """Bright lights blind you as PC Bacon unlocks your handcuffs and hands your over to Detective Lou
Tennant, they look at you like you’re a piece of chewing gum stuck to the sole of a shoe. With great
pleasure he throws you into the overnight cell and locks the door. \n
    --- \n
    GAME OVER.""",

    "exits":  {},

    "items": []
}

#Cab---------------------------------------------------------

room_cab = {
    "name": "Dragon Taxis",

    "description":
    """You get in the taxi and the aroma of faux leather overwhelms
your senses. Taxi driver with the ID reading \'Justin Sider\' turns
to you and asks Where would you like to go?.""",

    "exits": {"pryzm": "Pryzm",
              "glam": "Glam",
              "tiger": "Tiger Tiger",
              "lounge": "Live Lounge",
              "su": "SU",
              "kebab": "Kebab",
              "halls": "Halls",
              "kfc": "KFC"},

    "items": []
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


    "Pryzm": room_pryzm,
    "Pryzm Disco": room_pryzm_disco,
    "Pryzm Curve": room_pryzm_curve,
    "Pryzm House": room_pryzm_house,

    "McDonalds": room_mc,

    "KFC": room_kfc,

    "Alcohol Detention": room_detention,

    "Police": room_police,
    
    "Cab": room_cab

}



