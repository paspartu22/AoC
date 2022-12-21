import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}  

monkeys = {}
class Monkey:
    def __init__(self, result) -> None:
        self.result = result
        self.returner = 0
    
    def __str__(self):
        return f"{self.result}"
    
    def do_result(self):
        if len(self.result) == 1:
            return int(self.result[0])
        else:
            op_func = ops[self.result[1]]
            return op_func(monkeys[self.result[0]].do_result(), monkeys[self.result[2]].do_result()) 
    
    def do_root(self):
        left = monkeys[self.result[0]].do_result()
        right = monkeys[self.result[2]].do_result()
        return [left, right]
    
        
with open("data.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        #print (f" line {line}")
        monkeys[line[0][:-1]] = Monkey(line[1:])
        #print (monkeys[line[0][:-1]])
    last_diff = 0
    min = 0
    monkeys["humn"].result[0] = int(monkeys["humn"].result[0])
    max = monkeys["humn"].result[0]
    while (1):
        left, right = monkeys["root"].do_root()
        print(left-right)
        if left == right:
            print (f"!answer {monkeys['humn'].result[0]}")
            break
        else:
            if left < right:
                monkeys["humn"].result[0] = min + ((monkeys["humn"].result[0] - min) // 2)
                min = monkeys["humn"].result[0]
            else:
                monkeys["humn"].result[0] *= 2
                max = monkeys["humn"].result[0]
                

                
    #print (monkeys['root'].do_root())
        