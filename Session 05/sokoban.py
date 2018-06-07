map_sokoban = {
    "size_x": 5,
    "size_y": 5
}


player = {
    "x": 4,
    "y": 0
}

boxes = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 2},
    {"x": 3, "y": 3},

]


destinations =[
    {"x": 2, "y": 1},
    {"x": 3, "y": 1},
    {"x": 4, "y": 3}
    
]
playing = True
while playing:
# print map
# 2 vòng lặp đang chạy tọa độ
    for y in range(map_sokoban["size_y"]):
        for x in range(map_sokoban["size_x"]):

            box_is_here = False
            for box in boxes:
                if box['x'] == x and box['y'] == y:
                    # print("B ", end ="")
                    box_is_here = True
                    # break
            




            player_is_here = False
            if x==player["x"] and y == player["y"]:
                player_is_here = True
                # print("p ", end =" ")
            
            # elif box_is_here == False:

            #     print("- ", end=" ")
            dest_is_here = False
            for dest in destinations:
                if dest['x'] == x and dest['y'] == y:
                    dest_is_here = True

            if player_is_here:
                print("P ", end ="")
            elif box_is_here:
                print("B ", end="")
            elif dest_is_here:
                print("D ", end ="")
            else:
                print("- ", end="")   
        print()


    # end of print map
# Check win 
    # Check win
    win = True
    for box in boxes:
        if box not in destinations:
            win = False

    if win is True:
        print("You win!!")
        break
    dx = 0
    dy = 0


    move = input("Your move: ").upper()

    if move =="W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False
    if 0<= player['x'] + dx < map_sokoban['size_x'] \
     and 0<=player['y'] + dy < map_sokoban['size_y']:
     player['x'] += dx
     player['y'] += dy

    # MOve box:+
    for box in boxes:
        if box['x'] == player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box ['y'] += dy 

    



