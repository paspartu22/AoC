



with open("data.txt", "r") as file:
    set = {0:"", 1:"", 2:""}
    score = 0
        
    for i,line in enumerate(file):
        set[i%3] = line
        if i % 3 == 2:
            for letter in set[0]:
                if letter in set[1] and letter in set[2]:
                    score += ord(letter)- 96 if letter.islower() else ord(letter) - 38
                    break
    print(score)
    



    '''
    part 1
    score = 0
    with open("data.txt", "r") as file:
        for line in file:
            for letter in range(len(line)//2):
                if line[letter] in line[len(line)//2:]:
                    score += ord(line[letter])- 96 if line[letter].islower() else ord(line[letter]) - 38
                    break
        print(score) 
    '''