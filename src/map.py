__author__ = 'jake'

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

    "answer": "",

    "cost": 0
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

    "answer": "",

    "cost": 0
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
    "victory_points": 1,

    "special": "" ,

    "answer": "",

    "cost": 0
}

#Student Union ------------------------------------------------


room_su = {
    "name": "Outside Student's Union",

    "description":
    """You are standing outside the Students Union, entry costs £5, where do
you want to go?""",

    "exits":  {"south": "Live Lounge", "east": "Kebab", "cab": "Cab", "inside": "SU Tills"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}


room_su_pay = {
    "name": "SU Tills",

    "description":
    """You pay the entrance fee of £5 and can now enter the SU.""",

    "exits":  {"dancefloor": "SU Dancefloor", "bar": "SU Bar"},

    "items": [],

    "victory_points": 2,

    "special": """The female worker on the desk requires you to answer her 
question to prove you are a member of Cardiff University. She asks, 
"Which of the following is NOT a society that we offer here in Cardiff: 
The Gliding Society, The Coffee Society or The Sinatra Society?

Answer 'gliding', 'coffee' or 'sinatra'.""",

    "answer": "coffee",

    "cost": 5
}


room_su_dancefloor = {
    "name": "Student's Union Dancefloor",

    "description":
    """The cheap drinks have drawn you in. You look around Y Plas
and see a wallet on the floor. The bar is busy but well staffed and drinks
here are cheaper than elsewhere. What do you do next?""",

    "exits":  {"outside": "SU", "bar": "SU Bar"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
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

    "items": [item_sambuca_shot, item_tequila_shot, item_vodka, item_jagerbomb_shot, item_water], 

    "special": "",

    "answer": "",

    "cost": 0
}

#Tiger Tiger --------------------------------------------

room_tiger = {
    "name": "Tiger Tiger - The entrance",

    "description":
    """Do you dare enter Tiger Tiger for £5?""",

    "exits":  {"south": "McDonalds",
               "east":"Glam",
               "west":"Live Lounge",
               "cab": "Cab",
               "pay": "Tiger Tiger Tills"
               },

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}


room_tiger_pay = {
    "name": "Tiger Tiger Tills",

    "description":
    """You pay the entrance fee of £5 and can now enter the 
ever wonderful Tiger Tiger.""",

    "exits":  {"bar": "Tiger Tiger - The Club", "wonder": "Tiger Tiger - The Groovy Wonderland"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": "",

    "cost": 5
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

    "exits":  { "bar": "Tiger Tiger - The Club", "entrance": "Tiger Tiger"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}


room_tiger_club = {
    "name": "Tiger Tiger - The Club",

    "description":
    """You enter ‘The Club’ and your initial survey suggest that the Tiger Tiger 
management do indeed know what a club is. You notice a bag containing a mysterious
substance on the floor. You can pick up the package or leave it.""",

    "exits": {"wonder": "Tiger Tiger - The Groovy Wonderland", "entrance": "Tiger Tiger"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
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

    "answer": "",

    "cost": 0
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
potential trouble makers. Entry here costs £5.""",

    "exits":  {"south": "McDonalds", "east":"Pryzm Entrance", "west":"Tiger Tiger", "cab":"Cab", "pay": "Glam Tills"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}


room_glam_pay = {
    "name": "Glam Tills",

    "description":
    """You just paid the entrance fee, you can go in now! smile emoticon""",

    "exits":  {"inside": "Glam Bar"},

    "items": [],

    "victory_points": 2,

    "special": """You want to go into Glam but the bouncer is standing at the front door
blocking your way. "01001. What’s the password?" the guard asks you. 

You think for a second. A lad goes up to the bouncer. The bouncer says 
"00010". The lad replies "2" and is let in. 

A young lady approached a second later. The bouncer says 00101, she repies 5. 
She was also let in. 

You approach the bouncer again, "10011". What is your reply? """,

    "answer": "11",

    "cost": 5
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

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}

# Pryzm -------------------------------------------------
room_pryzm_entrance = {
    "name": "Pryzm Entrance",

    "description":
    """Long queues greet you at the Pryzm Entrance and you debate whether or not 
it is really a good idea to wait or whether you shoud go somewhere quieter. The 
choice is yours. Entry costs £5.""",

    "exits":  {"north": "Halls",
               "south": "McDonalds",
               "east": "KFC",
               "west": "Glam",
               "cab": "Cab",
               "pay": "Pryzm Tills"
               },

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": "",

    "cost": 0

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

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}


room_pryzm_pay = {
    "name": "Pryzm Tills",

    "description":
    """You pay the entrance fee of £5 and can now enter Pryzm.""",

    "exits":  {"inside": "Pryzm"},

    "items": [],

    "victory_points": 2,

    "special": "",

    "answer": "",

    "cost": 5
}


room_pryzm_disco = {
    "name": "Pryzm - The Disco area",

    "description":
    """Great choice. Only here can you do the Macarena and YMCA and not look like a 
total d*ck. Your mighty fine hips attract a plethora of female attention and before 
you know it you’ve pulled. Great work.""",

    "exits":  {"entrance": "Pryzm", "curve": "Pryzm Curve", "house": "Pryzm House"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}


room_pryzm_curve = {
    "name": "Pryzm - Curve area",

    "description":
    """Interesting choice. Many do not even know this room exists. You are rewarded 
with good music, a quiet(ish) bar and not being surrounded by \'Cheeky Archbishop of 
Banterbury Top Lads\' that you usually find in Pryzm.""",

    "exits":  {"entrance": "Pryzm", "house": "Pryzm House", "disco": "Pryzm Disco"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
}


room_pryzm_house = {
    "name": "Pryzm - House area",

    "description":
    """We’re not actually sure about the name of this room but it’s pretty busy and 
the strobe lighting probably isn\'t good for your epilepsy. You feel your health 
declining""",

    "exits":  {"entrance": "Pryzm", "curve": "Pryzm Curve", "disco": "Pryzm Disco"},

    "items": [],

    "victory_points": 0,

    "special": "",

    "answer": "",

    "cost": 0
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

    "items": [item_nuggets, item_big_mac, item_mcflurry, item_happy_meal],

    "victory_points": 1,

    "special": "",

    "answer": "",

    "cost": 0
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

    "answer": "",

    "cost": 0

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

    "answer": "",

    "cost": 0
}

#Cab---------------------------------------------------------

room_cab = {
    "name": "Dragon Taxis",

    "description":
    """You get in the taxi and the aroma of faux leather overwhelms your senses. 
Taxi driver with the ID reading \'Justin Sider\' turns to you and asks where you
would like to go?. Trips cost £5.""",

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

    "answer": "",

    "cost": 5
}


rooms = {
    "Your room": room_dorm,
    "Halls": room_halls,
    "Kebab": room_kebab,

    "SU": room_su,
    "SU Bar": room_su_bar,
    "SU Dancefloor": room_su_dancefloor,
    "SU Tills": room_su_pay,

    "Live Lounge": room_lounge,
    #"Live Lounge Bar": room_lounge_bar,

    "Tiger Tiger": room_tiger,
    "Tiger Tiger Tills": room_tiger_pay,
    "Tiger Tiger - The Groovy Wonderland": room_tiger_wonder,
    "Tiger Tiger - The Club": room_tiger_club,

    "Glam": room_glam,
    "Glam Bar": room_glam_bar,
    "Glam Tills": room_glam_pay,

    "Pryzm Entrance": room_pryzm_entrance,
    "Pryzm": room_pryzm,
    "Pryzm Tills": room_pryzm_pay,
    "Pryzm Disco": room_pryzm_disco,
    "Pryzm Curve": room_pryzm_curve,
    "Pryzm House": room_pryzm_house,

    "McDonalds": room_mc,

    "KFC": room_kfc,

    "Police": room_police,
    
    "Cab": room_cab

}



