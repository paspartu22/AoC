seq_len = 14
 
print (min([i if len(set(open("data.txt").readline()[i-seq_len :i])) == seq_len else len(open("data.txt").readline()) 
                                                        for i in range(seq_len-1, len(open("data.txt").readline()))]))

''' part 1 / 2
with open("data.txt") as file:
    for line in file:
        for i in range(seq_len-1, len(line)):
            if len(set(line[i-seq_len :i])) == seq_len:    
                print (i)
                break
'''