__author__ = 'ioana'

from items import *


room_halls = {
    "name": "University Halls",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_kebab = {
    "name": "Mama Kebab",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_su = {
    "name": "Student's Union",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_lounge = {
    "name": "Live Lounge",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_tiger = {
    "name": "Tiger Tiger",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_tiger_wonder = {
    "name": "Tiger Tiger - The Groovy Wonderland",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_tiger_club = {
    "name": "Tiger Tiger - The Club",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_glam = {
    "name": "Glam",

    "description":
    """Good ol Glam. Some love it, some hate it. You decided to come here so dont complain. You head
straight for the bar and look at the menu.""",

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_pryzm = {
    "name": "Pryzm",

    "description":
    """Ahh Pryzm, the staple club of any freshers night out. With a choice of music and a variety of bars
to choose from you feel content with your choice of club and feel that the long wait outside with the
ever annoying Paper reps was probably worth it.""",

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_pryzm_disco = {
    "name": "Pryzm - The Disco area",

    "description":
    """Great choice. Only here can you do the Macarena and YMCA and not look like a total d*ck. Your
mighty fine hips attract a plethora of female attention and before you know it youve pulled. Great
work.""",

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_pryzm_curve = {
    "name": "Pryzm - Curve area",

    "description":
    """Interesting choice. Many do not even know this room exists. You are rewarded with good music, a
quiet(ish) bar and not being surrounded by Cheeky Archbishop of Banterbury Top Lads that you
usually find in Pryzm.""",

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_pryzm_house = {
    "name": "Pryzm - House area",

    "description":
    """Were not actually sure about the name of this room but its
pretty busy and the strobe lighting probably isn't good for
your epilepsy.
-
Nope this really isnt helping your epilepsy. You collapse to
the floor and the room goes black. GAME OVER.""",

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_mc = {
    "name": "McDonalds",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_kfc = {
    "name": "KFC",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_detention = {
    "name": "Alcohol Detention Center",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}


room_police = {
    "name": "Police Station",

    "description":
    """   """,

    "exits":  {"north": "", "south": "", "east":"", "west":""},

    "items": []
}



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
    "House": room_pryzm_house,
}


