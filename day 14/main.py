
class Pos:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__ (self):
        return f"x {self.x} | y {self.y}"

    def check_up (self):
        if cave.get_dot(self.x, self.y - 1) and cave.get_dot(self.x - 1, self.y - 1) and cave.get_dot(self.x + 1, self.y - 1):
            return True
        else: 
            return False

class Line:
    def __init__ (self, x_start, x_finish, y_start, y_finish):
        self.dots = {}
        if x_start == x_finish:
            for y in range (min(y_start, y_finish), max(y_start, y_finish)+1):
                self.dots[x_start, y] = (Pos(x_start, y))
        else:
            for x in range (min(x_start, x_finish), max(x_start, x_finish)+1):
                self.dots[x, y_start] = (Pos(x, y_start))
                
    def __str__ (self):
        return f" line {self.dots}"

class Path:
    def __init__ (self, path):
        self.lines = []
        for i in range(len(path)-1):
            self.lines.append(Line(path[i][0], path[i+1][0], path[i][1], path[i+1][1]))

    def __str__ (self):
        return f"path {self.lines}"

class Cave:
    def __init__ (self):
        self.bottom = 0
        self.map = []
        self.rock = {}
        self.sand = {}

    def plain_rock (self):
        for path in self.map:
            for line in path.lines:
                for dot in line.dots:
                    if dot not in self.rock:
                        self.rock[dot] = 1

    def parse (self):
        with open("data.txt", "r") as file:
            for line in file:
                list_line = line.strip().split(" -> ")
                path = []
                for line in list_line:
                    x,y = line.split(",")
                    path.append([int(x), int(y)])
                    if self.bottom < int(y):
                        self.bottom = int(y)
            
                print (path)
                self.map.append(Path(path))
            self.bottom += 1
            print (self.bottom)
    
    def print_map(self):
        for rock in self.rock:
            print (rock)
    
    def get_dot (self, x, y):
        if (x, y) in self.rock or (x, y) in self.sand:
            return True

        return False
    
    def remove_dot(self, x, y):
        for path in self.map:
            for line in path.lines:
                for pos in line.dots:
                    if pos.x == x and pos.y == y:
                        line.dots.remove(pos)
        for sand in self.sand:
            if sand.x == x and sand.y == y:
                self.sand.remove(sand)
        
        print (f"remove {x} {y}")

class Sand (Pos):
    def __init__ (self, x = 500, y = 0):
        super().__init__(x, y)
    
    def move(self):
        if self.y == cave.bottom:
            return False
        elif not cave.get_dot(self.x, self.y+1):
            self.y += 1
            return True
        elif not cave.get_dot(self.x - 1, self.y + 1):
            self.y += 1
            self.x -= 1
            return True
        elif not cave.get_dot(self.x + 1, self.y + 1):
            self.x += 1
            self.y += 1
            return True
        else:
            '''
            if cave.get_dot(self.x, self.y + 1).check_up():
                cave.remove_dot(self.x, self.y + 1)
                
            if cave.get_dot(self.x - 1, self.y + 1).check_up():
                cave.remove_dot(self.x - 1, self.y + 1)

            if cave.get_dot(self.x + 1, self.y + 1).check_up():
                cave.remove_dot(self.x + 1, self.y + 1)
            '''
            return False
    
    def move_all(self):
        while (self.move()):
            continue
        cave.sand[self.x, self.y] = self
        if self.y == 0:
            return True
        else:
            return False



print ("start")
cave = Cave()
cave.parse()
cave.plain_rock()
cave.print_map()
print ()
result = 0
while (1):
    result += 1
    sand = Sand()
    if (sand.move_all()):
        #print(sand)
        break
    
    print(f"{result} {sand}")
print (result) #last one