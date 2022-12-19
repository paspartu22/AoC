
class Blueprint:
    def __init__ (self, ore, clay, obsidian, geode):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
    def __str__ (self):
        return f"ore {self.ore} clay {self.clay} obs {self.obsidian} geode {self.geode}"
        
            
class Game:
    def __init__ (self):
        self.bot = {"ore" : 1, "clay" : 0, "obsidian" : 0, "geode" : 0}
        self.resource = {"ore" : 1, "clay" : 0, "obsidian" : 0, "geode" : 0}
        self.moves = ["ore", "clay", "obsidian", "geode"]
    
    def choose_prode(self):
        return "ore"
    
    def move (self):
        production = self.choose_prod()
        
        for bot, amount in self.bot.items():
            self.resource[bot] += amount
            
        
        self.bot[production] += 1
        
game = Game()
blueprints = {}
with open("test.txt", "r") as file:
    for line in file:
        line = line.split()
        print(line)
        blueprints[int(line[1].strip(":"))] = Blueprint(int(line[6]), int(line[12]), [int(line[18]), int(line[21])], [int(line[27]), int(line[30])] )
        
for id, blueprint in blueprints.items():
    print(f"{id} | {blueprint}")