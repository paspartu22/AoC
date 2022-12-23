my_pos = [-1, -1]
my_dir = 0
vectors = {0: [1, 0], 1:[0, 1], 2:[-1, 0], 3:[0, -1]}
faces = {0 : [2,0], 1: [0,1], 2: }
class Cell:
    def __init__(self, x, y, can_move):
        self.x = x
        self.y = y
        self.can_move = True if can_move == "." else False
    
    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.can_move}"
    
    
class Map:
    def __init__(self):
        self.cells = {}
    
    def __iter__(self):
        for cell in self.cells.items():
            yield cell
        
    
    def get_next_cell(self):
        if (my_pos[0]+vectors[my_dir][0], my_pos[1]+vectors[my_dir][1]) in self.cells:
            return self.cells[(my_pos[0]+vectors[my_dir][0], my_pos[1]+vectors[my_dir][1])]
        else:
            output = None
            match my_dir:
                case 0:
                    for cell in self.cells:
                        if cell[1] == my_pos[1] and (output is None or cell[0] < output[0]):
                            output = cell
                case 1:
                    for cell in self.cells:
                        if cell[0] == my_pos[0] and (output is None or cell[1] < output[1]):
                            output = cell
                case 2:
                    for cell in self.cells:
                        if cell[1] == my_pos[1] and (output is None or cell[0] > output[0]):
                            output = cell
                case 3:
                    for cell in self.cells:
                        if cell[0] == my_pos[0] and (output is None or cell[1] > output[1]):
                            output = cell
            return self.cells[output]
        
    def print_map(self):
        pass

def do_move (moves_and_rotation):
    global my_pos
    global my_dir
    moves = int(moves_and_rotation[:-1])
    rot = moves_and_rotation[-1]
    for move in range(moves):
        next_cell = map.get_next_cell()
        if next_cell.can_move:
            my_pos = [next_cell.x,next_cell.y]
    
    if rot == "R":
        my_dir = (my_dir+1)%4
    else:
        my_dir = (my_dir-1)%4
        
def get_net_move (path):
    pass
    


map = Map()

with open ("data.txt", "r") as file:
    lines = file.readlines()
    for y,line in enumerate(lines):
        if line == "\n":
            break
        if my_pos == [-1,-1]:
            my_pos = [line.index("."),0]
        for x,char in enumerate(line.strip("\n")):
            if char != " ":
                map.cells[x,y] = (Cell(x,y,char))
                
    path = lines[-1]

    #for cell in map:
    #   print (cell[1])
    print (my_pos)
    print (path)
    while (len(path) > 0):
        R = path.index("R")+1 if "R" in path else len(path)
        L = path.index("L")+1 if "L" in path else len(path)
        ind = min(R,L)
        next_move = path[:ind]
        path = path[ind:] if ind < len(path) else ""
        if R == L:
            next_move += "R"
        #print(next_move)
        #print(path)
        do_move(next_move)
        print (my_pos)
    print (f" {my_pos} {my_dir-1}")
    print (f" Answer {((my_pos[1]+1)*1000)+((my_pos[0]+1)*4)+(my_dir-1)}")
    
    

    
    