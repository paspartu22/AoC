
class Sensor:
    def __init__(self, x, y, beacon_x, beacon_y):
        self.x = x
        self.y = y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y
    
    def __str__ (self):
        return f"X {self.x}, Y {self.y}, Be X {self.beacon_x}, Y {self.beacon_y}"
    
    
    def dist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)
    
    def safe_area (self, x, y):
        return (self.dist(self.beacon_x, self.beacon_y) >= self.dist(x, y))
    
    def perimeter (self):
        perimeter = []
        for side in range (4):
            for x in range (self.dist(self.beacon_x, self.beacon_y)+1):
                diff = [x, self.dist(self.beacon_x, self.beacon_y)+1 - x]
                match side:
                    case 0: perimeter.append([self.x + diff[0], self.y + diff[1]])
                    case 1: perimeter.append([self.x - diff[0], self.y - diff[1]])
                    case 2: perimeter.append([self.x - diff[0], self.y + diff[1]])
                    case 3: perimeter.append([self.x + diff[0], self.y - diff[1]])       
        return perimeter
                
                
        
def check_cell (x, y):
    for sensor in sensors:
        if sensor.beacon_x == x and sensor.beacon_y == y:
            return True
    for sensor in sensors:
        if sensor.safe_area(x, y):
            return True
    return False
 
sensors = []

with open("data.txt", "r") as file:
    min_x = None
    max_x = None
    for line in file:
        split_line = line.strip().split(" ")
        #print (split_line)
        sensor = Sensor(int(split_line[2][2:-1]), int(split_line[3][2:-1]), int(split_line[8][2:-1]), int(split_line[9][2:]))
        if min_x is None or min_x > sensor.beacon_x:
            min_x = sensor.beacon_x
        if max_x is None or max_x < sensor.beacon_x:
            max_x = sensor.beacon_x
        sensors.append(sensor)

    
    for sensor in sensors:
        print (sensor)
    
    result = 0
    y = 10
    y = 2_000_000
    area = 4_000_000
    #area = 20
    perimeters = []
    for sensor in sensors:
        perimeters.append(sensor.perimeter())
        print(len(sensor.perimeter()))
    for perimeter in perimeters:
        for dot in perimeter:    
            if not check_cell(dot[0], dot[1]) and 0 < dot[0] < area and 0 < dot[1] < area:
                print (dot[0]* 4_000_000 + dot[1])
    #print (perimeters)
            

