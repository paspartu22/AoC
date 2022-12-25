
vectors = {0: [1, 0], 1:[0, 1], 2: [-1, 0], 3: [0, -1], 4: [0, 0]}
width = 0
height = 0
blizzards = []
positions = {0 : [[1, 0]]}
move_num = 0


class Blizzard:
    def __init__ (self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
    
    def move (self):
        self.x += vectors[self.dir][0]
        self.y += vectors[self.dir][1]
        if self.x > width:
            self.x = 1
        elif self.x == 0:
            self.x = width
        if self.y > height:
            self.y = 1
        elif self.y == 0:
            self.y = height
            
    def __str__(self):
        return f"{self.x} {self.y} {self.dir}"
        
def print_map():
    s = "///"
    for x in range (width + 2):
        s += str(x) + " "
    print (s)
    for y in range(height + 2):
        s = str(y)+ "  "
        for x in range(width + 2):
            if any([position for position in positions[move_num] if position == [x, y]]):
                s += "E "
            elif get_cell(x, y):
                s += "# "
            else:
                s += ". "
        print (s)

def get_cell(x, y):
    for cell in blizzards:
        if cell.x == x and cell.y == y:
            return True
    return False
                
def do_move():
    for bliz in blizzards:
        bliz.move()
        
def avaliable_cells(pos):
    for my_pos in pos:
        if my_pos == [1, 1] or my_pos == [1, 0]:
            yield [1, 0]
        if my_pos == [width, height] or my_pos == [width, height+1]:
            yield [width, height+1]
        for vector in vectors.values():
            if (not get_cell(my_pos[0] + vector[0], my_pos[1] + vector[1]) and 
                0 < my_pos[0] + vector[0] <= width and  0 < my_pos[1] + vector[1] <= height):
                yield [my_pos[0] + vector[0], my_pos[1] + vector[1]]
    
        
with open ("data.txt", "r") as file:
    for y,line in enumerate(file):
        height = y
        width = len(line)
        for x,char in enumerate(line):
            match char:
                case ">":
                    blizzards.append(Blizzard(x, y, 0))
                case "<":
                    blizzards.append(Blizzard(x, y, 2))
                case "v":
                    blizzards.append(Blizzard(x, y, 1))
                case "^":
                    blizzards.append(Blizzard(x, y, 3)) 
    height -= 1
    width -= 2
print (height)
print (width)
path = {0: [width, height + 1], 1: [1, 0], 2: [width, height + 1]}
target = 0
print ("===INIT===")
print_map()
end = False
while (1):
    move_num += 1 
    print (f"==={move_num}===")

    do_move()
    
    positions [move_num] = list(avaliable_cells(positions[move_num-1]))
    output = []
    for x in positions[move_num]:
        if x not in output:
            output.append(x)
    positions[move_num] = output
    
    
    print (len(positions[move_num]))
    #print (positions)
    #print_map()
    for position in positions[move_num]:
        if position == path[target]:
            positions[move_num] = [position]
            target += 1
            break
    if target == 3 or len(positions[move_num]) == 0:
        print (f"ANSWER {move_num}")
        break
    
