

move_num = 0

move_done = False

vectors = {0 : [[-1,-1], [0, -1], [1, -1]],
           1 : [[1,  1], [0,  1], [-1, 1]],
           2 : [[-1,-1], [-1, 0], [-1, 1]],
           3 : [[1,  1], [1,  0], [1, -1]]}


class Elf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.my_move = [0, 0]
    
    def choose_move(self):
        self.my_move = [0, 0]
        
        if self.check_empty():
            return False    
                
        for i in range(4):
            dir = (i+move_num) % 4
            if self.check_vector(vectors[dir]):
                self.my_move = vectors[dir][1]
                return True
        
        return False

    def do_move(self):
        global move_done
        self.x += self.my_move[0]
        self.y += self.my_move[1]
        if self.my_move != [0, 0]:
            move_done = True
    
    def target_cell(self):
        return [self.x + self.my_move[0], self.y + self.my_move[1]]
        
                    
    def check_vector(self, vector):
        for dot in vector:
            if str([self.x+dot[0], self.y+dot[1]]) in game.elf_map:
               return False
        return True
    
    def check_empty(self):
        for i in range(4):
            if not self.check_vector(vectors[i]):
                return False
        return True
    
    def __str__(self) -> str:
        return f"{self.x} {self.y} "
    
    
class Game:
    def __init__(self):
        self.elves = []
        self.elf_map = {}
        
    def generate_map(self):        
        x_min, y_min = None, None
        x_max, y_max = None, None
        for elf in self.elves:
            if  x_min is None or elf.x < x_min:
                x_min = elf.x
            if y_min is None or  elf.y < y_min:
                y_min = elf.y
            if x_max is None or  elf.x > x_max:
                x_max = elf.x
            if y_max is None or  elf.y > y_max:
                y_max = elf.y 
                
        for y in range (y_min-1, y_max+2):
            for x in range(x_min-1, x_max+2):
                if str([x, y]) not in self.elf_map:
                    self.elf_map[x, y] = False
        for elf in self.elves:
            self.elf_map[str(elf.x, elf.y)] = True
        
    def update_map (self):
        sides = [] 
        for elf in self.elves:
            if  x_min is None or elf.x < x_min:
                x_min = elf.x
            if y_min is None or  elf.y < y_min:
                y_min = elf.y
            if x_max is None or  elf.x > x_max:
                x_max = elf.x
            if y_max is None or  elf.y > y_max:
                y_max = elf.y 
        self.elf_map = {}
                
        for side in range (y_min-1, y_max+2):
            for x in range(x_min-1, x_max+2):
                if str([x, y]) not in self.elf_map:
                    self.elf_map[x, y] = False
                    

    def choose_move(self):
        for elf in self.elves:
            elf.choose_move()
            
    def compare_move(self):
        map_of_moves = []
        for elf in self.elves:
            map_of_moves.append(elf.target_cell())
        for elf in self.elves:
            if len([move for move in map_of_moves if move == elf.target_cell()]) > 1:
                elf.my_move = [0, 0]
                
    
    def do_move(self):
        for elf in self.elves:
            elf.do_move()
        
    def __iter__(self):
        for elf in self.elves:
            yield elf
    
    def score_finale(self):
        x_min, y_min = None, None
        x_max, y_max = None, None
        for elf in self.elves:
            if  x_min is None or elf.x < x_min:
                x_min = elf.x
            if y_min is None or  elf.y < y_min:
                y_min = elf.y
            if x_max is None or  elf.x > x_max:
                x_max = elf.x
            if y_max is None or  elf.y > y_max:
                y_max = elf.y 
                
        print (f"{(x_max - x_min + 1) * (y_max - y_min + 1) - len(self.elf_map)}")

    def print_game(self):
        print (f" ======= MOVE {move_num} =========")
        print (f"Main dir = {(move_num-1) % 4}")
        print (f"Amount of elves {len(self.elf_map)}")
        x_min, y_min = None, None
        x_max, y_max = None, None
        for elf in self.elves:
            if  x_min is None or elf.x < x_min:
                x_min = elf.x
            if y_min is None or  elf.y < y_min:
                y_min = elf.y
            if x_max is None or  elf.x > x_max:
                x_max = elf.x
            if y_max is None or  elf.y > y_max:
                y_max = elf.y
        
        print (f"X {x_min} {x_max} Y {y_min} {y_max}")
        s = "    "
        for x in range(x_min-1, x_max+2):
            s += f"{x}"
            if len(str(x)) == 1 or x == -1:
                s += " "
        print (s)
        for y in range (y_min-1, y_max+2):
            s = ""
            if y >= 0:
                s += " "
            s += f"{y} |  "
            s = s[:5]
            for x in range(x_min-1, x_max+2):
                if str([x, y]) in self.elf_map:
                    s += "# "
                else:
                    s += ". "
            print (s)
        print ("------")
        print ()

game = Game()
with open("data.txt", "r") as file:
    for y,line in enumerate(file):
        for x,char in enumerate(line):
            if char == "#":
                game.elves.append(Elf(x, y))

game.generate_map()
game.print_game()
while (1):
    
    move_done = False
    game.choose_move()
    game.compare_move()
    game.do_move()
    game.update_map()
    move_num += 1
    game.print_game()
    print (f" Move {move_num}")
    if not move_done:
        break

print ("FINAL STATE")
game.score_finale()
print(move_num)
    