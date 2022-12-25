
other_base = ["=", "-", "0", "1", "2"]
base = {"=" : -2, "-" : -1, "0" : 0, "1" : 1, "2" : 2}
result = 0


with open ("data.txt", "r") as file:
    for line in file:
        number = 0
        for i,char in enumerate(line.strip("\n")):
        #    print (char)
            power = 5**(len(line.strip("\n"))-i-1)
        #    print (power)
            number += base[char]*power
        print (number)
        result += number

print (f" ANSWER {result}")
max_power = 0
while (1):
    if 5**(max_power) * 2.5 > result:
        break
    else:
        max_power += 1

print (f"Max_power {max_power}")
string_result = ""
for i in range (max_power, -1, -1):
    for x in range (-2, 3):
        if abs(result - (x * (5 ** i))) <= (5 ** i) // 2:
            string_result += other_base[x+2]
            result -= x * (5 ** i)
            break

print (result)
print (string_result)