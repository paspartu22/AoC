import numpy as np 

class Pos:
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self, dir): 
        match(dir):
            case("U"): self.y += 1
            case("D"): self.y -= 1
            case("R"): self.x += 1
            case("L"): self.x -= 1

class Rope:
    def __init__(self, lenght): #create 10 knot rope
        self.knots=[]
        for i in range(lenght):
            self.knots.append(Pos())
            
    def move_next(self, head, tail): #move tail knot after head knot 
        if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
            tail.x += np.sign(head.x - tail.x)
            tail.y += np.sign(head.y - tail.y)
            return True
        else:
            return False
            
    def move_rope(self): # move every knot from 1 to 9 (not the head)
        for i in range(1, len(self.knots)):
            if not self.move_next(self.knots[i-1],self.knots[i]):
                break
    
rope = Rope(10)
visited = [] #visited cells by tail

def check_visited():
    if [rope.knots[-1].x, rope.knots[-1].y] not in visited:
        visited.append([rope.knots[-1].x, rope.knots[-1].y])

def main ():   
    with open ("data.txt", "r") as file:
        for line in file:
            for i in range(int(line.split(" ")[1])):
                rope.knots[0].move(line.split(" ")[0])
                rope.move_rope()                
                check_visited()
                
        print (len(visited))

main()