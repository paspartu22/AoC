
class directory:
    def __init__ (self, name):
        name = name
        content = {}



with open("test.txt", "r") as file:
    directorys = {directory("/")}
    current_dir = "/"
    for line in file:
        if line.split()[0] == "$":
            if line.split()[1] == "cd":
                if line.split()[2] == "..":
                    continue #go out
                elif line.split()[2] == "/":
                    continue #go /
                else:
                    continue #new directory
                
        elif line.split()[0] == "dir":
            directorys[current_dir].content[line ]
        else:
            continue #add file
        