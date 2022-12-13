

def parse (string):
    output = []
    level = 0
    start = -1
    string = string[1:-1]
    
    for i,letter in enumerate(string):
        if letter.isdigit() and level == 0:
            if letter.isdigit:
                result = int(letter)
                if i>0 and string[i-1].isdigit():
                    last = output.pop()
                    output.append(last*10+result)
                else:
                    output.append(result)
        elif letter == "[":
            if level == 0:
                start= i
            level += 1
        elif letter == "]":
            level -=1
            if level == 0:
                output.append(parse(string[start:i+1]))
                start = -1
    return output

def compare (item1, item2):
    i = 0
    while(1):
        if i == len(item1):
            if i != len(item2):
                return True
            else:
                return None
        elif i == len(item2):
            return False
            
        elif isinstance (item1[i], int) and isinstance(item2[i], int):
            if item1[i] < item2[i]:
                return True
            elif item1[i] > item2[i]:
                return False
        else:
            if isinstance (item1[i], int): item1[i] = [item1[i]]
            if isinstance (item2[i], int): item2[i] = [item2[i]]
            rec = compare(item1[i], item2[i])
            if rec is not None:
                return rec
        i += 1



with open ("data.txt", "r") as file:
    pairs = [k.split('\n') for k in file.read().split('\n\n')]
    samples = []
    for pair in pairs:
        sample = []
        for item in pair:
            
            sample.append(parse(item))
        samples.append(sample)
    
    # part 2
    plain_samples = []
    for pair in samples:
        plain_samples.append(pair[0])
        plain_samples.append(pair[1])
    samples = plain_samples
    
    #BUBLESOTR
    
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1,len(samples)):
            if not compare(samples[i-1],samples[i]):
                samples[i],samples[i-1] = samples[i-1],samples[i]
                sorted = False
    
    packet1 = [[2]]
    packet2 = [[6]]
    
    for i,sample in enumerate(samples[1:]):
        if compare(packet1, sample) and compare(samples[i], packet1):
            #print(packet1)
            loc1 = i
        if compare(packet2, sample) and compare(samples[i], packet2):
            #print(packet2)
            loc2 = i
        
        print (sample)
        
    print((loc1+2)*(loc2+3)) # +1 becouse of num, +1 becouse of counter from 1, +1 becouse of prev insertion
    
    
                
            
    '''    part 1
    result = 0
    for i,sample in enumerate(samples[:]):
        
        print (sample[0])
        print (sample[1])
        
        if compare(sample[0],sample[1]):
            result += (i+1)
        print(compare(sample[0],sample[1]))
        print("---")
  
    print(result)
    '''      