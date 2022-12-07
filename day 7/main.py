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
                    path.append(line.split()[2])
                    dirname = "/"
                    for dir in path:
                        if dir != "/":
                            dirname += dir+"/"
                    if dirname not in dirs:
                        dirs[dirname] = 0

        elif line.split()[0].isdigit():
            dirname = "/"
            for dir in path:
                if dir != "/":
                    dirname += dir+"/"
                dirs[dirname] += int(line.split()[0])
                
    print(dirs)
    ''' part 1
    output = 0
    for weight in dirs.values():
        if weight <= 100000:
            output += weight
    print (output)
    '''
    # part 2
    space_need = abs(70000000 - 30000000 - dirs["/"])
    print(space_need)
    min_dir = "/"
    for dir in dirs:
        if space_need < dirs[dir] < dirs[min_dir]:
            min_dir = dir
    print (f"Dir:{min_dir} space {dirs[min_dir]}")