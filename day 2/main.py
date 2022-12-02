
moves_1 = {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}
moves_2 = {"A" : 1, "B" : 2, "C" : 3, "X" : 0, "Y" : 3, "Z" : 6}
score = 0

with open ("day 2/input.txt", "r") as file:
    print ( sum ( [(moves_2[line[2]] + (moves_2[line[0]] - 1 + (moves_2[line[2]]//3 - 1)) % 3 + 1) for line in file]))
    
    ''' part 2
    for line in file:
        score += moves_2[line[2]] + (moves_2[line[0]] - 1 + (moves_2[line[2]]//3 - 1)) % 3 + 1 # -1 drop to base3, -1 to 
        print (f"{moves_2[line[0]]} {moves_2[line[2]]} {(moves_2[line[0]] - 1 + (moves_2[line[2]]//3 - 1)) % 3 + 1}")
    '''        
    ''' 
    part 1
        en_move = moves_1[line[0]]
        my_move = moves_1[line[2]]
        #print(f"{en_move} | {my_move}")
        score += my_move
        if (my_move - en_move) % 3 == 1:
            score += 6
        elif (my_move == en_move):
            score += 3
    print (f"My score {score}")
    
    '''