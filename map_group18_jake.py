__author__ = 'ioana'

from items import *

#Halls --------------------------------------------------------

entrance_halls = {
    "name": "Outside University Halls",

    "description":
    """You are standing outside your halls. Where do you want to go?""",

    "exits":  {"south": "Pryzm", "west": "Mama Kebab", "cab": "Cab", "inside": "University Halls"},

    "items": []
} #Not done as i dont have a clue what i'm doing

#Mama Kebab ---------------------------------------------------

room_kebab = {
    "name": "Mama Kebab",

    "description":
    """Good choice. Kfw (Kebab for the win). You have a choice of buying a 
    ‘Thick Sausage Kebab’ or a ‘Long Sausage Kebab’. Mama is getting impatient,
    what are you going to go for?""",

    "exits":  {"west": "SU", "east": "University Halls" , "cab": "Cab"},

    "items": [] #possible need list or dictionary of kebabs?
}

#Student Union ------------------------------------------------

outside_su = {
    "name": "Outside Student Union",

    "description":
    """You are standing outside the Students Union, entry costs £5, where do 
    you want to go?""",

    "exits":  {"south": "Live Lounge", "east": "Mama Kebab", "cab": "Cab", "inside": "Student Union"},

    "items": []
}

room_su = {
    "name": "Student Union Foyer",

    "description":
    """The cheap drinks have drawn you in. You look around Y Plas 
    and see a wallet on the dancefloor. The bar is busy but well staffed and drinks 
    here are cheaper than elsewhere. What do you do next?""",

    "exits":  {"bar": "Student Union Bar", "wallet": "Student Union Dancefloor", "cab": "Cab", "entrance": "Outside Student Union"},

    "items": []
}

room_su_bar = {
    "name": "Student Union Bar",

    "description":
    """CUSU Menu:\n 
    Sambuca - £1\n
    Tequila - £1\n
    Vodka - £1\n
    Jagerbomb - £2\n
    Water - Free\n
    The young bar man looks at you, “What do you want Fresher?” """,

    "exits":  {"cab": "Cab", "entrance": "Outside Student Union", "foyer": "Student Union Foyer"},

    "items": [] #need to add dictionary of drinks?
}

room_su_wallet = {
    "name": "Student Union Dancefloor",

    "description":
    """You pick up the wallet and find that there is no money in it. But what did you 
    expect? You’re in the SU full of very broke students! You do however find an expired 
    condom still in its foil wrapper. You keep the condom as a precaution and toss the 
    wallet back on the floor continuing with your night.""",

    "exits":  {"cab": "Cab", "entrance": "Outside Student Union", "foyer": "Student Union Foyer"},

    "items": ['Expired Condom'] #not sure this is right. are we even keeping this or going to change it for a different item?
}

#Live Lounge ---------------------------------------------------

outside_lounge = {
    "name": "Outside Live Lounge",

    "description":
    """You are standing outside Live Lounge, entry costs £5, where do 
    you want to go?""",

    "exits":  {"north": "SU", "east": "Tiger Tiger", "cab": "Cab", "inside": "Live Lounge"},

    "items": []
}

room_lounge = {
    "name": "Live Lounge Foyer",

    "description":
    """As soon as you approach the bar, you see Kirill and Matt doing Russian Standard shots 
    counting in binary. Do you go upstairs and avoid? Or join them at the bar?""",

    "exits":  {"entrance": "Outside Live Lounge", "cab": "Cab", "bar": "Live Lounge Bar", "upstairs": "Upstairs Live Lounge"},

    "items": []
}

room_lounge_bar = {
    "name": "Live Lounge Bar",

    "description":
    """- 001 shot down.\n
    - 010 shots down.\n
    - 011 and you begin to regret this decision but it’s too late to leave now.\n
    - 100 shots.\n
    - 101.\n
    - 111.........and spew. You projectile vomit across the bar.\n
    Matt and Kirill continue drinking laughing at your feeble attempt to keep 
    up with them. \n
    - GAME OVER!"""
} #would like to add a timer to delay each shot taken here.

room_lounge_upstairs = {
    "name": "Upstairs Live Lounge",

    "description":
    """You move to the other side of the floor away from the two doctors and go upstairs. A wise move, they 
    are doing more shots than you could ever handle. What would you like to do next?""",

    "exits":  {"cab": "Cab", "foyer": "Live Lounge Foyer", "outside": "Outside Live Lounge"},

    "items": []
}

#Tiger Tiger --------------------------------------------------

outside_tiger = {
    "name": "Outside Tiger Tiger",

    "description":
    """You are standing outside Tiger Tiger, entry costs £5, where do 
    you want to go?""",

    "exits":  {"north": "SU", "east": "Tiger Tiger", "cab": "Cab", "inside": "Tiger Tiger Foyer"},

    "items": []

room_tiger = {
    "name": "Tiger Tiger Foyer",

    "description":
    """Inside Tiger Tiger you have three choices. Go to the ‘Groovy Wonderland’, ‘The Club’ or back outside.""",

    "exits":  {"Groovy Wonderland": "The Groovy Wonderland", "Club": "The Club", "outside": "Outside Tiger Tiger", "cab": "Cab"},

    "items": []
}

room_tiger_wonder = {
    "name": "The Groovy Wonderland",

    "description":
    """Really? 80s Disco anthems? You have no choice to crack out some killer moves but people don’t 
    seem impressed. After a while a police officer approaches. “Excuse me sir”, he interrupts you mid 
    hip thrust, “We have had reports of criminal dance moves in this establishment tonight”. A wave 
    of embarrassment rushes over you, you knew you shouldn’t have gone for the moon walk. He slaps the 
    cuffs around your wrists and takes you to the police station.""",

    "exits":  {},

    "items": [] #need a 'go to police station' funtion.
}

room_tiger_club = {
    "name": "The Club",

    "description":
    """You enter ‘The Club’ and your initial survey suggest that the Tiger Tiger management do indeed
know what a club is. You notice a bundle of glow sticks on the floor and go to pick them up but you
don’t have room to fit them in your pockets, you’ll need to swap either your ID, Phone or Keys to fit
them in. What are you going to choose?""",

    "exits":  {"foyer": "Tiger Tiger Foyer", "outside": "Outside Tiger Tiger", "cab": "Cab"},

    "items": ['Glow Sticks'] #again i'm not sure this is right. also we need to find a use for the glow sticks or something
}

#Glam ------------------------------------------------------

entrance_glam = {
    "name": "Outside Glam",

    "description":
    """You are standing outside Glam, entry costs £5, where do 
    you want to go?""",

    "exits":  {"south": "McDonalds", "east": "Pryzm", "west": "Tiger Tiger", "cab": "Cab", "inside": "Glam"},

    "items": []
}

room_glam = {
    "name": "Glam",

    "description":
    """Good ol’ Glam. Some love it, some hate it. You decided to come here so don’t complain.
    There isn't much going on here so you head straight for the bar and look at the menu.\n
    Glam Menu:\n
    WKD - £3\n
    Vodka - £2\n
    Desperados - £3\n
    Jack Daniels - £3\n
    Water - Free""",

    "exits":  {"outside": "Outside Glam", "cab": "Cab"},

    "items": [] #do we need a list or dictionary of drinks here?
}

#Pryzm -------------------------------------------------------

entrance_pryzm = {
    "name": "Outside Pryzm",

    "description":
    """You are standing outside Glam, entry costs £5, where do 
    you want to go?""",

    "exits":  {"north": "Halls", "south": "McDonalds", "east": "KFC", "west": "Glam", "cab": "Cab", "inside": "Pryzm Foyer"}

    "items": []
}}

room_pryzm = {
    "name": "Pryzm Foyer",

    "description":
    """Ahh Pryzm, the staple club of any freshers night out. With a choice of music and a variety of bars
to choose from you feel content with your choice of club and feel that the long wait outside with the
ever annoying Paper reps was probably worth it. You have a choice of going to the Disco Room, the House 
Room or the Curve Room, or you can go back outside.""",

    "exits":  {"outside": "Outside Pryzm", "disco": "Disco Room", "curve": "Curve Room", "house": "House Room", "cab": "Cab"},

    "items": []
}


room_pryzm_disco = {
    "name": "Disco Room",

    "description":
    """Great choice. Only here can you do the Macarena and YMCA and not look like a total d*ck. Your
mighty fine hips attract a plethora of female attention and before you know it you’ve pulled. Great
work. +20 health points""",

    "exits":  {"foyer": "Pryzm Foyer", "outside": "Outside Pryzm", "cab": "Cab"},

    "items": []
}


room_pryzm_curve = {
    "name": "Curve Room",

    "description":
    """Interesting choice. Many do not even know this room exists. You are rewarded with good music, a
quiet(ish) bar and not being surrounded by the ‘Archbishop of Banterbury Top Lads’ that you
usually find in Pryzm. +1 point""",

    "exits":  {"foyer": "Pryzm Foyer", "outside": "Outside Pryzm", "cab": "Cab"},

    "items": []
}


room_pryzm_house = {
    "name": "House Room",

    "description":
    """We’re not actually sure about the name of this room but it’s
pretty busy and the strobe lighting probably isn't good for
your epilepsy.\n
---\n
Nope this really isn’t helping your epilepsy. You collapse to
the floor and the room goes black. 
GAME OVER.""",
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

    "items": []
} #need to add the 'would you like fries with that', im not sure how.

#KFC ----------------------------------------------------------

room_kfc = {
    "name": "KFC",

    "description":
    """You arrive to the locked doors of KFC, tears dripping down your
face you collapse into a heap on the floor. You should have
known that KFC closes at 11:00pm but you didn’t think it
through. How can you continue with your night after this great
ordeal?! \n
-----\n
GAME OVER.""",

}

#Alcohol Detention Centre -----------------------------------

room_detention = {
    "name": "Alcohol Detention Center",

    "description":
    """Uh-oh. You shouldn’t have had that last drink. You got way too drunk and now you’re in the alcohol
detention centre. They gave you magical medicine, you can now continue your night. Your health
has been restored to 100%, but your points have been affected badly. A cab comes to pick you up from outside.""",

    "exits":  {"cab":"Cab"},

    "items": []

#Police Station ---------------------------------------------

room_police = {
    "name": "Police Station",

    "description":
    """Bright lights blind you as PC Bacon unlocks your handcuffs and hands your over to Detective Lou
    Tennant, they look at you like you’re a piece of chewing gum stuck to the sole of a shoe. With great
    pleasure he throws you into the overnight cell and locks the door.\n
    --- \n
    GAME OVER."""
}

#Dictionaries of Rooms --------------------------------------

rooms = {
    "Halls": room_halls,
    "Kebab": room_kebab,
    "SU": room_su,
    "Live Lounge": room_lounge,
    "Tiger Tiger": room_tiger,
    "Glam": room_glam,
    "Pryzm": room_pryzm,
    "McDonalds": room_mc,
    "KFC": room_kfc,
    "Alcohol Detention": room_detention,
    "Police": room_police
}

rooms["Tiger Tiger"] = {
    "wonder": room_tiger_wonder,
    "club": room_tiger_club
}

rooms["Pryzm"] = {
    "Disco": room_pryzm_disco,
    "Curve": room_pryzm_curve,
    "House": room_pryzm_house
}

rooms["SU"] = {
    "Bar": room_su_bar,
    "Wallet": room_su_wallet
}

rooms["University Halls"] = {}

 # im not sure what the bottom bits are about so im gonna leave them 
 #for now. im so shit at this coding thing.

