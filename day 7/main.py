path = []
dirs = {"/" : 0}

with open("data.txt", "r") as file:
    for line in file:
        #print (line.split())
        if line.split()[0] == "$":
            if line.split()[1] == "cd":
                if line.split()[2] == "..":
                    path.pop()
                elif line.split()[2] == "/":
                    path = ["/"]
                else:
                    dirname = line.split()[2]
                    while dirname in dirs:
                        dirname += "_"
                    
                    path.append(dirname)
                    dirs[dirname] = 0

        elif line.split()[0].isdigit():
            for dir in path:
                dirs[dir] += int(line.split()[0])
                
    print(dirs)
    output = 0
    for weight in dirs.values():
        if weight <= 100000:
            output += weight
    print (output)