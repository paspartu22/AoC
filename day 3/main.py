



#lines = open("data.txt", "r").readlines()

print(sum([max([(ord(letter)- 96 if letter.islower() else ord(letter) - 38) 
                        if letter in open("data.txt", "r").readlines()[i+1] and letter in open("data.txt", "r").readlines()[i+2] else 0 for letter in line])
                                    if i%3 == 0 else 0 for i,line in enumerate(open("data.txt", "r").readlines())]))



'''

set = {}

score_2 = [ord(letter)- 96 if letter.islower() else ord(letter) - 38 for letter in set[0] if i%3==2 else 0 set[i%3] for i,line in enumerate(open("data.txt","r"))]
print 
for i,line in enumerate(open("data.txt", "r")):
    set[i%3] = line
    if i % 3 == 2: 
        for letter in set[0]:
            if letter in set[1] and letter in set[2]:
                score_2[i] = ord(letter)- 96 if letter.islower() else ord(letter) - 38
                break
print(score_2)
print(sum(score_2))
'''


'''


score = 0
with open("data.txt", "r") as file:
    for line, letter in file:
        print (line)
        print (letter)
        for letter in range(len(line)//2):
            if line[letter] in line[len(line)//2:]:
                score += ord(line[letter])- 96 if line[letter].islower() else ord(line[letter]) - 38
                break
    print(score) 
'''