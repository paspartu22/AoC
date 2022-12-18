
vectors = [[0,0,1],[0,0,-1],
           [0,1,0],[0,-1,0],
           [1,0,0],[-1,0,0]]



LAVA = 0
AIR = 1

class Cell:
    def __init__ (self, x, y, z, type):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.type = type
        self.connect = []


    def __str__(self) -> str:
        return f"{self.type} X {self.x} Y {self.y} Z{self.z} Con {len(self.connect)}"




    def connect_cell (self):
        for vector in vectors:
            point = [self.x + vector[0], self.y + vector[1], self.z + vector[2]]
            if str(point) in cells:
                self.connect.append(cells[str(point)])
            elif self.type == LAVA:
                air_cells[str(point)] = Cell(*point, AIR)



def bfs (start):
    visited = []
    queue = []
    queue.append([start])
    
    while queue:
        path = queue.pop(0)        
        node = path[-1]
                
        for vector in vectors:
            neibor = [node[0]+vector[0], node[1]+vector[1], node[2]+vector[2]]

            if (neibor not in visited and str(neibor) not in cells and 
                -1 <= neibor[0] <= 22 and -1 <= neibor[1] <= 22 and -1 <= neibor[2] <= 22):
                
                new_path = list(path)
                new_path.append(neibor)
                queue.append(new_path) 
                visited.append(neibor)
    return visited

air_cells = {}
big_blob = [[0,0,0]]
cells = {}
min_x, min_y, min_z = None, None, None
max_x, max_y, max_z = None, None, None
with open ("data.txt", "r") as file:
    for line in file:
        x,y,z = line.split(",")
        if min_x is None or min_x > int(x):
            min_x = int(x)
        if max_x is None or max_x < int(x):
            max_x = int(x)
        if min_y is None or min_y > int(y):
            min_y = int(y)
        if max_y is None or max_y < int(y):
            max_y = int(y)
        if min_z is None or min_z > int(z):
            min_z = int(z)
        if max_z is None or max_z < int(z):
            max_z = int(z)
        cells[str([int(x), int(y), int(z)])] = Cell(x,y,z, LAVA)
print (f"X {min_x} {max_x}")
print (f"Y {min_y} {max_y}")
print (f"Z {min_z} {max_z}")
result = 0
for key,cell in cells.items():
    cell.connect_cell()
    print (f"{key} | {cell}")
    result += 6 - len(cell.connect)
print (f"Part 1 {result}")
print ("==================")
#part 2
print ("Calculating big air...")
big_blob = bfs([0,0,0])
print (len(big_blob))
open_air = {}
for cell in big_blob:
    if str(cell) in air_cells:
        open_air[str(cell)] = air_cells[str(cell)]
        #print (cell)
print (len(air_cells))
print (len(open_air))
result = 0
for key,cell in open_air.items():
    cell.connect_cell()
    result += len(cell.connect)
    print (f"{key} | {cell}")
    
print (f"Part 2 {result}")

