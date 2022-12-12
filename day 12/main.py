
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


    def check_cell (self, x, y):
        if map.get_cell(x, y) and map.get_cell(x, y).h - self.h >= -1: # <=1 for forward movment, >= -1 for backtrace
            return True
        else:
            return False

    def check_neibors(self):
        if self.check_cell(self.x + 1, self.y):
            self.possible_moves.append(map.get_cell(self.x + 1, self.y))

        if self.check_cell(self.x - 1, self.y):
           self.possible_moves.append(map.get_cell(self.x - 1, self.y))

        if self.check_cell(self.x, self.y + 1):
            self.possible_moves.append(map.get_cell(self.x, self.y + 1))

        if self.check_cell(self.x, self.y - 1):            
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
                        self.finish = Pos(row, col, letter)

                    if letter == "S":
                        letter = "a"
                        self.start = Pos(row,col, letter)

                    self.cells.append(Pos(row, col, letter))
        
    def add_connections(self):
        for cell in self.cells:
            cell.check_neibors()
            #print (cell)
            
    def bfs (self, start, finish):
        
        queue = []
        visited = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            
            print (len(path))
            node = path[-1]
            if node in finish: 
                return len(path)-1
            
            for neibor in node.possible_moves:
                if neibor not in visited:
                    
                    new_path = list(path)
                    new_path.append(neibor)
                    queue.append(new_path) 
                    visited.append(neibor)


map = Map()
def main():
    map.parce_input()
    map.add_connections()
    #print(map.bfs(map.get_cell(map.start.x, map.start.y), map.get_cell(map.finish.x, map.finish.y))) part 1
    print(map.bfs(map.get_cell(map.finish.x, map.finish.y), [cell for cell in map.cells if cell.h == 0]))

if __name__ == '__main__':
    main()
