
room_lock = {
    "Room": [19,9],
    "Halls": [19, 7],
    "Mama Kebab": [14, 7],

    "  SU": [8, 7],
    

    "Live Lounge": [8, 5],
    

    "Tiger Tiger": [13, 5],
    
    

    "Glam": [19,5],
    

    "Pryzm Entrance": [24, 5],
    

    "McDonalds": [18, 3],

    "KFC": [30, 5],

    "Police": [10, 1],
    
    "Cab": [2, 1]
    }
    
def map_creation():
    array_mapx = [[0 for x in range(33)] for x in range(10)]
    for x in range(0,10):
        for y in range(0,33):
            array_mapx[x][y] = " "
    for val in room_lock:
    
        if len(val) > 5:        
            for x in range(0,5):
                array_mapx[room_lock[val][1]][room_lock[val][0]-2+ x] = val[x]
    
        else:
            for x in range(0,len(val)):
                 array_mapx[room_lock[val][1]][room_lock[val][0]-2 + x] = val[x]
    array_mapx[8][19] = "|"
    array_mapx[5][27] = "-"
    array_mapx[7][16] = "-"
    array_mapx[7][11] = "-"
    array_mapx[5][10] = "-"
    array_mapx[6][8] = "|"
    array_mapx[5][16] = "-"
    array_mapx[4][18] = "|"
    array_mapx[5][16] = "-"
    array_mapx[5][21] = "-"
    array_mapx[4][21] = "/"
    array_mapx[6][10] = "\\"
    array_mapx[4][16] = "\\"
    array_mapx[6][22] = "\\"



    for val in range(0,10):
        array_mapx[val] = "".join(array_mapx[val])
    
    for val in range(9,0,-1):
        print(array_mapx[val])