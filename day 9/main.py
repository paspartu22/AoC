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
    def __init__(self):
        knots=[]
        for i in range(10):
            knots.append(Pos())
        
  

head = Pos()
tail = Pos()

def move_tail():
    dist = abs(head.x - tail.x) + abs(head.y - tail.y)
    match(dist):
        case(2):
            if head.x == tail.x:
                if head.y > tail.y:
                    tail.move("U")
                else:
                    tail.move("D")
            elif head.y == tail.y:
                if head.x > tail.x:
                    tail.move("R")
                else:
                    tail.move("L")
        case(3):
            if head.x > tail.x:
                tail.move("R")
            else:
                tail.move("L")
            if head.y > tail.y:
                tail.move("U")
            else:
                tail.move("D")

visited = []

with open ("data.txt", "r") as file:
    for line in file:
        print (line)
        for i in range(int(line.split(" ")[1])):
            head.move(line.split(" ")[0])
            print (f"HEAD {head.x} {head.y}")
            move_tail()
            print (f"TAIL {tail.x} {tail.y}")
            if [tail.x, tail.y] not in visited:
                visited.append([tail.x, tail.y])

    print (len(visited))
