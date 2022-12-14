class Monkey:
    def __init__ (self, id, items, inspect_eq, test_number, target_on_true, target_on_false):
        self.id = id
        self.items = items
        self.inspect_eq = inspect_eq
        self.test_number = test_number
        self.target_on_true = target_on_true
        self.target_on_false = target_on_false
        self.number_of_inspetions = 0
    
    def __str__ (self):
        return (f"id {self.id}| inspect_eq {self.inspect_eq}| test_number {self.test_number}| target_on_true {self.target_on_true}| target_on_false {self.target_on_false}| items {self.items}|")
    
    def inspect_item(self, item):
        if item > common_delimiter:
            item = item % common_delimiter
        self.number_of_inspetions += 1
        a = item
        b = int(self.inspect_eq[2:]) if self.inspect_eq[2].isdigit() else item
        if self.inspect_eq[1] == "*":
            return (a*b)
        elif self.inspect_eq[1] == "+":
            return (a+b)
    
    def test_item(self, item):
        if item % self.test_number == 0:
            self.throw_item(self.target_on_true, item)
        else:
            self.throw_item(self.target_on_false, item)
    
    def throw_item(self, target, item):
        monkeys.monkeys_list[target].items.append(item)
        self.items.pop(0)
        #print (f"Monkey {self.id} throw item to {target}")
    
    def process_items(self):
        while self.items:
            self.items[0] = self.inspect_item(self.items[0])
            self.test_item(self.items[0])

class Monkeys:
    def __init__(self):
        self.monkeys_list = []
    
    def process_round(self):
        for monkey in self.monkeys_list:
            monkey.process_items()

    def parse_monkeys(self):
        with open("data.txt", "r") as file:
            for line in file:
                #print(line)
                if line == "\n":
                    self.monkeys_list.append(Monkey(id,items, inspect_eq, test_number, target_on_true, target_on_false,))
                else:
                    line = line.strip().split()
                    if line[0] == "Monkey":
                        id = line[1][0]
                    elif line[0] == "Starting":
                        items = []
                        for item in line[2:]:
                            items.append(int(item.strip(",")))
                    elif line[0] == "Operation:":
                        sign = line[-2]
                        b = line[-1] if line[-1].isdigit() else "i"
                        inspect_eq = "i"+sign+b
                    elif line[0] == "Test:":
                        test_number = int(line[-1])
                    elif line[1] == "true:":
                        target_on_true = int(line[-1])
                    elif line[1] == "false:":
                        target_on_false = int(line[-1])
            #last one
            self.monkeys_list.append(Monkey(id,items, inspect_eq, test_number, target_on_true, target_on_false,))

monkeys = Monkeys()
common_delimiter = 1

def main ():
    
    monkeys.parse_monkeys()
    global common_delimiter
    for monkey in monkeys.monkeys_list:
        common_delimiter *= monkey.test_number
        print(monkey)
    print(common_delimiter)

    for round in range(10000):
        #print (f"Round {round}")
        monkeys.process_round()
        #for monkey in monkeys.monkeys_list:
            #print(f"id: {monkey.id}| items {monkey.items}")

    numbers = []
    for monkey in monkeys.monkeys_list:
        numbers.append(monkey.number_of_inspetions)
        print (f"Monkey {monkey.id} number of inspections {monkey.number_of_inspetions}")
    numbers.sort()
    print (f"Monkey buisness {numbers[-1]*numbers[-2]}")

if __name__ == '__main__':
    main()