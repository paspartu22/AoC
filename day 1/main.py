import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

with open("day 1/input.txt", "r") as file:
    cur_elf = 0
    max_elf = []
    for line in file:
        #print (cur_elf)
        if len(line) >  1:
            cur_elf += int(line[:])
        else:
            if len(max_elf) < 3:
                max_elf.append(cur_elf)
                max_elf.sort()
                print (max_elf)
            elif cur_elf > max_elf[0]:
                max_elf[0] = cur_elf
                max_elf.sort()
                print (max_elf)
            cur_elf = 0

print (f"max {sum(max_elf)}")