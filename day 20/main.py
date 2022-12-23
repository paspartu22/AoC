

array = []
with open("data.txt", "r") as file:
    for i, line in enumerate(file):
        array.append((int(line)*811589153, i))

#array.append(-4)
new_array = array.copy()
#print(array)
for asd in range(10):
    print (asd) 
    for i,num in enumerate(array):
        index = new_array.index(num)
        new_array.pop(index)
        new_index = index + num[0]

        
        new_index %= len(array) - 1
        if new_index == 0:
            new_index = len(array)
        
        new_array.insert(new_index, num)
        #if num != new_array.index(num)-index + loop*(len(array)-1):
        #diff = abs(num[0] - new_array.index(num[0])-index) % (len(array)-1)
        #print (f"{i} | {index} {new_index} || {diff}")
        #print (new_array)

for i,index in enumerate(new_array):
    if index[0] == 0:
        zero_index = i
        break

result = 0
for i in range (1,4):
    result += new_array[(i*1000+zero_index) % len(new_array)][0]
print (f" Len {len(array)}")
print (f" result {result}")
