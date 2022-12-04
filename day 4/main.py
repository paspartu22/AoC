
import re

result = 0

with open ("data.txt", "r") as file:
    for line in file:
        elf1_start_str, elf1_finish_str, elf2_start_str, elf2_finish_str = re.split(",|-",line)
        elf1_start,elf1_finish, elf2_start,elf2_finish = int(elf1_start_str), int(elf1_finish_str), int(elf2_start_str), int(elf2_finish_str)
        if elf2_start <= elf1_start <= elf2_finish or elf1_start <= elf2_start <= elf1_finish:
            print (line.strip())
            result += 1

    print (result)










''' part1
with open("data.txt", "r") as file:
    for line in file:
        elf1_start,elf1_finish, elf2_start,elf2_finish = re.split(",|-",line)
        if (int(elf1_start) - int(elf2_start)) * (int(elf2_finish) - int(elf1_finish)) >= 0:
            print (f"count {elf1_start} {elf1_finish} and {elf2_start} {elf2_finish}")
            result += 1
    print (result) 
'''