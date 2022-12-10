

sprites = {1:"██", 0:"░░"}
addx = 1
cash = 0
eta = 1
line = ""

with open ("data.txt", "r") as file:
    for clk in range(240):

        eta -= 1
        if eta == 0:
            addx += cash
            data_line = file.readline().strip().split(" ")
            #print (data_line)
            
            if data_line[0] == "noop":
                eta = 1
                cash = 0
            else:
                eta = 2
                cash = int(data_line[1])

        if abs((clk % 40)- addx) <= 1:
            line += sprites[1]
        else:
            line += sprites[0]
        if (clk % 40) == 39:
            print(line)
            line = ""   
        