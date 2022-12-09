import numpy as np 

class Pos:
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self, dir): 
        match(dir):
            case("U"):
                self.y += 1
            case("D"):
                self.y -= 1
            case("R"):
                self.x += 1
            case("L"):
                self.x -= 1

class Rope:
    def __init__(self): #create 10 knot rope
        self.knots=[]
        for i in range(10):
            self.knots.append(Pos())
            
    def move_tail(self, head, tail): #move tail knot after head knot 
        if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
            tail.x += np.sign(head.x - tail.x)
            tail.y += np.sign(head.y - tail.y)
            
    def move_rope(self): # move every knot from 1 to 9 (not the head)
        for i in range(1, 10):
            self.move_tail(self.knots[i-1],self.knots[i])
    
rope = Rope()  
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