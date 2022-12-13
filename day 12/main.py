import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib import cm
from matplotlib.ticker import LinearLocator


class Pos:
    def __init__(self, x, y, letter, end = False) -> None:
        self.x = x
        self.y = y
        self.h = ord(letter)-97
        self.end = end
        self.visited = False
        self.possible_moves = []
    def __str__(self) -> str:
        return f"X {self.x}| Y {self.y}| H {self.h}| moves {len(self.possible_moves)}"


    def check_cell (self, x, y, dir = "up"):
        if dir == "up":
            if map.get_cell(x, y) and map.get_cell(x, y).h - self.h <= 1: # <=1 for forward movment, >= -1 for backtrace
                return True
        else:
            if map.get_cell(x, y) and map.get_cell(x, y).h - self.h >= -1: # <=1 for forward movment, >= -1 for backtrace
                return True
        return False


    def check_neibors(self, dir):
        self.possible_moves = []
        if self.check_cell(self.x + 1, self.y, dir):
            self.possible_moves.append(map.get_cell(self.x + 1, self.y))

        if self.check_cell(self.x - 1, self.y, dir):
           self.possible_moves.append(map.get_cell(self.x - 1, self.y))

        if self.check_cell(self.x, self.y + 1, dir):
            self.possible_moves.append(map.get_cell(self.x, self.y + 1))

        if self.check_cell(self.x, self.y - 1, dir):            
            self.possible_moves.append(map.get_cell(self.x, self.y - 1))


class Map:
    def __init__(self):
        self.cells = []

        self.start = Pos(0, 0, "a")
        self.finish = Pos(0, 0, "a")
        
    
    def get_cell(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def parce_input(self):
        with open("data.txt", "r") as file:
            for row,line in enumerate(file):
                for col, letter in enumerate(line.strip()):
                    if letter == "E":
                        letter = "z"
                        self.cells.append(Pos(row, col, letter))
                        self.finish = self.get_cell(row, col)

                    if letter == "S":
                        letter = "a"
                        self.cells.append(Pos(row, col, letter))
                        self.start = self.get_cell(row, col)

                    self.cells.append(Pos(row, col, letter))
        
    def add_connections(self, dir):
        for cell in self.cells:
            cell.check_neibors(dir)
            #print (cell)
            
    def bfs (self, start, finish):
        
        queue = []
        visited = []
        queue.append([start])
        
        while queue:
            #draw_map()
            path = queue.pop(0)
            
            print (len(path))
            node = path[-1]
            
            if isinstance(finish, list):
                if node in finish:
                    return path
            else:
                if node == finish: 
                    return path
            
            for neibor in node.possible_moves:
                if neibor not in visited:
                    
                    new_path = list(path)
                    new_path.append(neibor)
                    queue.append(new_path) 
                    visited.append(neibor)
    
def draw_map(path = []):
       
        
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    heights = []
    x = np.arange(0, 41, 1)
    y = np.arange(0, 67, 1)
    X, Y = np.meshgrid(y, x)
    for row in range (41):
        line = []
        for col in range (67):
            color = map.get_cell(row, col).h

            if map.get_cell(row,col) in path:
                color +=1
            line.append(color)
       
        heights.append(line)
    Z = np.array([np.array(h) for h in heights])
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_zlim(0, 27)
    
    #im = ax.imshow(heights)
    plt.show()        


map = Map()
def main():
    
    map.parce_input()
    map.add_connections("up")
    draw_map()
    path = map.bfs(map.start, map.finish)
    draw_map(path)
    print(len(path)-1)
       
    print ("Part 2")
    map.parce_input()
    map.add_connections("down")
    path = map.bfs(map.finish, [cell for cell in map.cells if cell.h == 0])
    draw_map(path)    
    print(len(path)-1)

if __name__ == '__main__':
    main()
