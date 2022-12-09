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
                
    def __str__(self) -> str:
        return f"{self.x} {self.y}"

class Rope:
    def __init__(self):
        self.knots=[]
        for i in range(10):
            self.knots.append(Pos())
            
    def move_tail(self, head, tail):
        if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
            tail.x += np.sign(head.x - tail.x)
            tail.y += np.sign(head.y - tail.y)
            
    def move_rope(self):
        for i in range(1, 10):
            self.move_tail(self.knots[i-1],self.knots[i])


rope = Rope()  

visited = [] #visited cells by tail

with open ("data.txt", "r") as file:
    for line in file:
        for i in range(int(line.split(" ")[1])):
            print()
            print (line)
            rope.knots[0].move(line.split(" ")[0])
            print (f"HEAD {rope.knots[0]}")
            
            rope.move_rope()
            print (f"TAIL {rope.knots[-1]}")

            if [rope.knots[-1].x, rope.knots[-1].y] not in visited:
                visited.append([rope.knots[-1].x, rope.knots[-1].y])

    print (len(visited))
