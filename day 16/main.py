

class Cave:
    def __init__(self, name, flow, paths) -> None:
        self.name = name 
        self.flow = flow
        self.str_path = paths
        self.path = []
    
    def get_connections(self):
        self.path = [caves.caves[path] for path in self.str_path]

    def __str__(self):
        return f"{self.name} flow {self.flow} path {self.path}"
    

class Caves:
    def __init__(self):
        self.caves = {}

    def __iter__(self):
        for cave in self.caves.values():
            yield cave
    
    def bfs(self, start, finish):
        queue = []
        visited = []
        queue.append([start])
        
        while queue:
            #draw_map()
            path = queue.pop(0)
            
            #print (len(path))
            node = path[-1]
            
            if isinstance(finish, list):
                if node in finish:
                    return path
            else:
                if node == finish: 
                    return path
            
            for neibor in node.path:
                if neibor not in visited:
                    
                    new_path = list(path)
                    new_path.append(neibor)
                    queue.append(new_path) 
                    visited.append(neibor)

caves = Caves()


with open ("test.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        path = [path.strip(",") for path in line[9:]]
        flow = int(line[4].split("=")[1].strip(";"))

        caves.caves[line[1]] = Cave(line[1], flow, path)

for cave in caves:
    cave.get_connections()
    #print (cave)

def get_value (start, target, time):
    move_after = time - (len(caves.bfs(start,target))-1) - 1
    return  [move_after *target.flow, move_after ] if move_after > 0 else [0, 0]



def depthFirst(graph, currentVertex, visited):

    visited.append(currentVertex)

    for vertex in graph:
        if vertex not in visited and vertex.flow > 0:
            yield from (depthFirst(graph, vertex, visited.copy()))
            
    if len(visited) > len(graph.caves):
        yield visited

    
        
visitedList = [cave for cave in caves if cave.flow == 0]
items_to_remove = len(visitedList)
for item in visitedList:
    print(item)
    
traversal = list(depthFirst(caves, caves.caves["AA"], visitedList))
print(f'Nodes visited in this order: {len(traversal)}')
results = []
for i,line in enumerate(traversal):
    if i % 1000 == 0:
        print (i)
    line = line[items_to_remove:]
    s = "AA -> "
    time = 30
    result = [[0, time]]
    for i,point in enumerate(line[1:]):
        if result[-1][1] > 0:
            result.append(get_value(line[i], point, result[-1][1]))
        
        s += point.name + " -> "

    #print(s)
    
    #print (result)
    sum_result = 0
    for point in result:
        sum_result += point[0]
    #print (sum_result)
    results.append(sum_result)

print ()
print(max(results))
    
    

