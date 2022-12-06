'''
[B]                     [N]     [H]
[V]         [P] [T]     [V]     [P]
[W]     [C] [T] [S]     [H]     [N]
[T]     [J] [Z] [M] [N] [F]     [L]
[Q]     [W] [N] [J] [T] [Q] [R] [B]
[N] [B] [Q] [R] [V] [F] [D] [F] [M]
[H] [W] [S] [J] [P] [W] [L] [P] [S]
[D] [D] [T] [F] [G] [B] [B] [H] [Z]
 1   2   3   4   5   6   7   8   9 
 '''

crates = {1:["D","H","N","Q","T","W","V","B"],
          2:["D","W","B"],
          3:["T","S","Q","W","J","C"],
          4:["F","J","R","N","Z","T","P"],
          5:["G","P","V","J","M","S","T"],
          6:["B","W","F","T","N"],
          7:["B","L","D","Q","F","H","V","N"],
          8:["H","P","F","R"],
          9:["Z","S","M","B","L","N","P","H"]} #hardcoded

stack = {} #parcing

with open ("data.txt", "r") as file:
    lines = []
    while 1:
        lines.append(file.readline())
        if lines[-1][0] == " ":
            break
    for index,letter in enumerate(lines[-1]):     
        if letter.isdigit():
            stack[letter] = ""
            for i in range(len(lines)-2,-1,-1):
                if lines[i][index].isupper() :
                    stack[letter] += lines[i][index] 
                    
    print (stack) 
    print (file.readline())
    while 1:
        line = file.readline().strip()
        if line == "":
            break
        else:   
            
            _,amount,_,start,_,finish = line.split(" ")
            amount = int(amount)
            
            print (f"{line} {amount} {start} {finish}")
            print (f"Grab {amount} from {start}. Its {stack[start][-amount:]}")
            
            stack[finish] += stack[start][-amount:]
            stack[start] = stack[start][:-amount]
            
            print (stack[start])

    output = ""
    for col in stack.values():
        output += col[-1]
    print (output)