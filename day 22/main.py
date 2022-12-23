my_pos = [0, 0, 0]
my_dir = 0
dir_chars = {0 : ">", 1: "v", 2: "<", 3: "^"}
vectors = {0: [1, 0], 1:[0, 1], 2:[-1, 0], 3:[0, -1]}
##test 

#faces = {0 : [2, 0], 1 : [0, 1], 2 : [1, 1], 
#         3 : [2, 1], 4 : [2, 2], 5 : [3, 2]}
#face_lenght = 4

### data
faces = {0 : [1, 0], 1 : [2, 0], 2 : [1, 1], 
         3 : [0, 2], 4 : [1, 2], 5 : [0, 3]}
face_lenght = 50

class Cell:
    def __init__(self, x, y, owner, can_move):
        self.x = x
        self.y = y
        self.owner = owner
        self.can_move = True if can_move == "." else False
    
class Face:
    def __init__(self, id):
        self.id = id 
        self.cells = {}
        self.connect_out = {}
        self.connect_type = {}
        
    def print_face(self):
        print (f"== Face {self.id} ===")
        for y in range (face_lenght):
            s = ""
            for x in range(face_lenght):
                if my_pos[2] == self.id and my_pos[0] == x and my_pos[1] == y:
                    s += dir_chars[my_dir] 
                elif self.cells[x, y].can_move:
                    s += "."
                else:
                    s += "#"
            print (s)
    
    def return_cross_face_cell(self, id, cell):
        for i,face in self.connect_out.items():
            if face.id == id:
                new_dir = (i + 2) % 4
                if not self.connect_type[i % 4]:
                    cell = face_lenght - cell - 1
                break

        match new_dir:
            case 0:
                return [self.cells[0, cell], new_dir]
            case 1:
                return [self.cells[cell, 0], new_dir]
            case 2:
                return [self.cells[face_lenght-1, cell], new_dir]
            case 3:
                return [self.cells[cell, face_lenght-1], new_dir]
                
                
    
    def get_next_cell(self):
        if 0 <= my_pos[0] + vectors[my_dir][0] < face_lenght and 0 <= my_pos[1] + vectors[my_dir][1] < face_lenght:
            return self.cells[(my_pos[0] + vectors[my_dir][0], my_pos[1] + vectors[my_dir][1])]
        else:
            cell = my_pos[0] if my_dir % 2 == 1 else my_pos[1]
            return self.connect_out[my_dir].return_cross_face_cell(self.id ,cell)
                    
        
class Map:
    def __init__(self):
        self.faces = {0: Face(0), 1: Face(1), 2: Face(2) ,3: Face(3), 4: Face(4), 5: Face(5)}
    
    def parse_input(self):     
        with open ("data.txt", "r") as file:
            lines = file.readlines()
            for y,line in enumerate(lines):
                if line == "\n":
                    break
                for x,char in enumerate(line.strip("\n")):
                    if char != " ":
                        face = 0
                        for num,location in faces.items():
                            if location[0]*face_lenght <= x < (location[0]+1)*face_lenght and location[1]*face_lenght <= y < (location[1]+1)*face_lenght:
                                face = num
                                break
                        self.faces[face].cells[x % face_lenght, y % face_lenght] = (Cell(x % face_lenght,y % face_lenght, face, char))
            
            self.path = lines[-1]
    
    def get_moves(self):
        self.list_path = []
        last_digit = 0
        for i,char in enumerate(self.path):
            if char.isupper():
                self.list_path.append(self.path[last_digit:i+1])
                last_digit = i+1
        self.list_path.append(self.path[last_digit:]+"E")
        #print (self.list_path)
                
    def connect_testfaces(self):
        self.faces[0].connect_out  = {0 : self.faces[5], 1: self.faces[3], 2: self.faces[2], 3: self.faces[1]}
        self.faces[0].connect_type = {0 : False,         1: True,          2: True,          3: False}
        self.faces[1].connect_out  = {0 : self.faces[2], 1: self.faces[4], 2: self.faces[5], 3: self.faces[0]}
        self.faces[1].connect_type = {0 : True,          1: False,         2: False,         3: False}
        self.faces[2].connect_out  = {0 : self.faces[3], 1: self.faces[4], 2: self.faces[1], 3: self.faces[0]} 
        self.faces[2].connect_type = {0 : True,          1: False,         2: True,          3: True}     
        self.faces[3].connect_out  = {0 : self.faces[5], 1: self.faces[4], 2: self.faces[2], 3: self.faces[0]}
        self.faces[3].connect_type = {0 : False,         1: True,          2: True,          3: True}
        self.faces[4].connect_out  = {0 : self.faces[5], 1: self.faces[1], 2: self.faces[2], 3: self.faces[3]}
        self.faces[4].connect_type = {0 : True,          1: False,         2: False,         3: True}
        self.faces[5].connect_out  = {0 : self.faces[0], 1: self.faces[1], 2: self.faces[4], 3: self.faces[3]} 
        self.faces[5].connect_type = {0 : False,         1: False,         2: True,          3: False}   
    
    def connect_faces(self):
        self.faces[0].connect_out  = {0 : self.faces[1], 1: self.faces[2], 2: self.faces[3], 3: self.faces[5]}
        self.faces[0].connect_type = {0 : True,          1: True,          2: False,         3: True}
        self.faces[1].connect_out  = {0 : self.faces[4], 1: self.faces[2], 2: self.faces[0], 3: self.faces[5]}
        self.faces[1].connect_type = {0 : False,         1: True,          2: True,          3: True}
        self.faces[2].connect_out  = {0 : self.faces[1], 1: self.faces[4], 2: self.faces[3], 3: self.faces[0]} 
        self.faces[2].connect_type = {0 : True,          1: True,          2: True,          3: True}     
        self.faces[3].connect_out  = {0 : self.faces[4], 1: self.faces[5], 2: self.faces[0], 3: self.faces[2]}
        self.faces[3].connect_type = {0 : True,          1: True,          2: False,         3: True}
        self.faces[4].connect_out  = {0 : self.faces[1], 1: self.faces[5], 2: self.faces[3], 3: self.faces[2]}
        self.faces[4].connect_type = {0 : False,         1: True,          2: True,          3: True}
        self.faces[5].connect_out  = {0 : self.faces[4], 1: self.faces[1], 2: self.faces[0], 3: self.faces[3]}
        self.faces[5].connect_type = {0 : True,          1: True,          2: True,          3: True}
        
    def __iter__(self):
        for face in self.faces.values():
            yield face
            
    def print_map(self):
        global my_pos
        global my_dir
        
        
    def get_next_cell(self):
        return self.faces[my_pos[2]].get_next_cell()
        
    def do_move (self, moves_and_rotation):
        global my_pos
        global my_dir
        moves = int(moves_and_rotation[:-1])
        rot = moves_and_rotation[-1]
        
        for move in range(moves):
            next_cell = self.get_next_cell()
            if isinstance(next_cell, list):
                if next_cell[0].can_move:
                    my_pos = [next_cell[0].x, next_cell[0].y, next_cell[0].owner]
                    my_dir = next_cell[1]                    
                    #self.faces[my_pos[2]].print_face()
            else:
                if next_cell.can_move:
                    my_pos = [next_cell.x, next_cell.y, my_pos[2]]
                    #self.faces[my_pos[2]].print_face()

        
        if rot == "R":
            my_dir = (my_dir+1)%4
        elif rot == "L":
            my_dir = (my_dir-1)%4
            
        #print (moves_and_rotation)
        
def get_net_move (path):
    pass
    


def main ():
    map = Map()
    map.parse_input()
    
    #for face in map:
    #    face.print_face()
    #print (map.path)
    map.connect_faces()
    map.get_moves()
    for move in map.list_path:
        map.do_move(move)
        
    row = my_pos[1] + ((faces[my_pos[2]][1]) * face_lenght) + 1
    col = my_pos[0] + ((faces[my_pos[2]][0]) * face_lenght) + 1
    print (f"{my_pos} {row} {col} {my_dir} resuilt {1000*row + 4*col + my_dir}")

   
    
if __name__ == "__main__":
    main()
