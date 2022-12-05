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
          9:["Z","S","M","B","L","N","P","H"]}

with open ("data.txt", "r") as file:
    print ("start")
    for line in file:
        split = line.split(" ")
        amount = int(split[1])
        start = int(split[3])
        finish = int(split[5])
        print (f"{line} {amount} {start} {finish}")
        for num in range(amount):
            print(f"grab {crates[start][-amount+num]}")
            print(crates[start])
            print(crates[finish])
            crates[finish].append(crates[start][-amount+num])
            crates[start].pop(-amount+num)

    for stack in crates.values():
        print(stack[-1])