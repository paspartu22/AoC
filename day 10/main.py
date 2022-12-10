
sprites = {1:"██", 0:"░░"}

#sprites = {1:"#", 0:"."}

clk = 1
strenght = 1
values = {}

print ("start")
with open ("data.txt", "r") as file:

    for line in file:
        print (line.split(" "))
        if line.strip().split(" ")[0] == "noop":
            clk += 1
        else:
            clk += 2
            strenght += int(line.split(" ")[1])
            values[clk] = strenght
            
    print (values)
    result = 0
    screen = []
    line = []
    sprite_pos = 1
    for clk in range(1, 242):
        if (clk-1) % 40 == 0:
            screen.append(line)
            line = []
        if clk in values:
            sprite_pos = values[clk]

        if abs(((clk-1) % 40) - sprite_pos) <= 1:
            line.append(sprites[1])
        else:
            line.append(sprites[0])



    for line in screen:
        str_line = ""
        for item in line:
            str_line += item
        print(str_line)
        
    ''' part 1
    start_key = [20, 60, 100, 140, 180, 220]
    for start in start_key:
        real_key = start
        while real_key not in values:
            real_key -= 1
        result += start * values[real_key]
        print(f"Line {start} strenght {values[real_key]}")
    print(result)
    '''