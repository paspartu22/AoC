seq_len = 14

with open("data.txt") as file:
    for line in file:
    #line = file.readline()
        print(line)
        for i in range(seq_len-1, len(line)):
            if len(set(line[i-seq_len :i])) == seq_len:    
                print (i)
                break