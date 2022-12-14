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
        return left-right
    
        
with open("data.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        #print (f" line {line}")
        monkeys[line[0][:-1]] = Monkey(line[1:])
        #print (monkeys[line[0][:-1]])

    monkeys["humn"].result[0] = int(monkeys["humn"].result[0])
    #3352886133831
    #print(monkeys["root"].do_root())
    #print()       
for i in range(5):
    diff = monkeys["root"].do_root()
    print(f" off by {diff}")
    monkeys["humn"].result[0] += 100
    new_diff = monkeys["root"].do_root()
    print (f" off +100 {new_diff}")
    diff_for_one = diff -  new_diff
    print(f" off by 100 do {diff_for_one}")
    print (f"current {monkeys['humn'].result[0]} delta {new_diff/diff_for_one*100}")
    monkeys["humn"].result[0] += new_diff/diff_for_one*100
    print(f" off after {monkeys['root'].do_root()}")
    print(f"answer {monkeys['humn'].result[0]}")

                
    #print (monkeys['root'].do_root())
        