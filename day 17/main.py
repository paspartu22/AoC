
from collections import OrderedDict

rock_shape = {  0: [[0,0], [1,0], [2,0], [3,0]], 
                1: [[1,0], [0,1], [1,1], [2,1], [1,2]],
                2: [[0,0], [1,0], [2,0], [2,1], [2,2]],
                3: [[0,0], [0,1], [0,2], [0,3]],
                4: [[0,0], [0,1], [1,1], [1,0]]}
rock_width = {0: 3, 1:2, 2:2, 3:0, 4:1}
    
def check_move (rock, dir, type):
    rock_x, rock_y = rock[0]
    match dir:
        case "<":
            rock_x -= 1
        case ">":
            rock_x += 1
        case "d":
            rock_y -=  1
    rock_width = {0: 3, 1:2, 2:2, 3:0, 4:1}
    rock_width = rock_width[type]
    if rock_x < 0 or rock_y < 0 or rock_x + rock_width > 6: #check for walls
        return False
    for dot in rock[1]:
        if rock_y+dot[1] in rocks and (rock_x+dot[0] in rocks[rock_y+dot[1]]):
                return False
    return True
    
def move (rock, dir, type):
    if dir == "<":
        if check_move(rock, dir, type):
            rock[0][0] -= 1
            return True
    elif dir == ">":
        if check_move(rock, dir, type):
            rock[0][0] += 1
            return True
    else:
        if check_move(rock, dir, type):
            rock[0][1] -= 1
            return True
    
    return False

move_num = 0

def move_all (rock, type):
    global move_num
    while (1):
        #print_map(rock)
        move(rock, line[move_num % len(line)], type)
        move_num += 1
        if move_num > len(line):
            move_num -= len(line)
        if not move(rock, "d", type):
            
            for dot in rock[1]:
                if rock[0][1] + dot[1] in rocks:
                    rocks[rock[0][1] + dot[1]].append(rock[0][0] + dot[0])
                else:
                    rocks[rock[0][1] + dot[1]] = [rock[0][0] + dot[0]]
            break


line = open ("data.txt", "r").readline().strip()
print (line)
rocks = {-1:[-1]} # [0,0] in global 
rocks_coordinate = {0:[],1:[],2:[],3:[],4:[]}

def print_map(rock):
    
    print (f" MOVE {move_num}")
    #print (rocks)
    print(line[move_num])
    max_y = (max(rocks))
    for y in range (max_y+5, -1, -1):
        s = f"{y}\t|"
        for x in range (0,7):
            if ((y in rocks and x in rocks[y]) or
                any([[x - rock[0][0], y- rock[0][1]] == dot for dot in rock[1]])):
                s += "#"
            else:
                s += "."
        print (s + "|")
    print (f"\t---------")
    print ()



big = 100_000
#big = 2022

for i in range (big):
    if i % 1000 == 0:
        print (f"rock {i}")

    max_y = max(rocks)
    type = i%len(rock_shape)
    rock = [[2,max_y+4], rock_shape[type]]
    move_all(rock, type)
    rocks_coordinate[type].append(rock[0])
    #print_map(rock)

print (max(rocks)+1)

with open('output_for_data.txt', 'w') as f:
    for i in range(len(rocks_coordinate[0])):
        s = ""
        for j in range (len(rocks_coordinate)):
            s += str(rocks_coordinate[j][i][0]) + ";" + str(rocks_coordinate[j][i][1]) + ";"
        f.write(s + "\n")
