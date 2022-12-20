import re

class Monkey:

    def __init__(self):
        self.monkey_number = 0
        self.items = []
        self.operation = None
        self.divisible_by = 0
        self.true_monkey = None
        self.false_monkey = None
        self.inspection_count = 0

    def parse_monkey(self, monkey_data, other_monkeys):
        self.monkey_number = int(re.search('Monkey (\d+):', monkey_data[0]).group(1))
        starting_items = re.search("Starting items: (.*)", monkey_data[1]).group(1)
        if "," in starting_items:
            self.items = [int(item) for item in starting_items.split(", ")]
        else:
            self.items = [int(starting_items)]
        self.operation = re.search("Operation: new = (.*)", monkey_data[2]).group(1)
        self.divisible_by = int(re.search("Test: divisible by (\d*)", monkey_data[3]).group(1))
        true_monkey_num = int(re.search("If true: throw to monkey (\d*)", monkey_data[4]).group(1))
        self.true_monkey = other_monkeys[true_monkey_num]
        false_monkey_num = int(re.search("If false: throw to monkey (\d*)", monkey_data[5]).group(1))
        self.false_monkey = other_monkeys[false_monkey_num]

    def throw_items(self, worry_divider=0, is_auto_manage_worry=True):
        for old in self.items:
            self.inspection_count += 1
            worry_level = eval(self.operation)
            if is_auto_manage_worry:
                worry_level = worry_level // 3
            else:
                worry_level = worry_level % worry_divider
            if worry_level % self.divisible_by == 0:
                self.true_monkey.add_item(worry_level)
            else:
                self.false_monkey.add_item(worry_level)
        self.items = []

    def get_monkey_number(self):
        return self.monkey_number

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)

    def get_operation(self):
        return self.operation

    def get_divisible_by(self):
        return self.divisible_by

    def get_true_monkey(self):
        return self.true_monkey

    def get_false_monkey(self):
        return self.false_monkey

    def get_inspection_count(self):
        return self.inspection_count

def main():
    input_file = open('input/day11.txt', 'r')
    monkeys_input = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    monkeys_data = extract_monkeys_data(monkeys_input)
    monkeys = parse_monkeys(monkeys_data)
    throw_items(monkeys, 20)
    monkeys_activity = get_monkeys_activity(monkeys)
    
    print("Answer 1: {}".format(monkeys_activity[0] * monkeys_activity[1]))

    monkeys = parse_monkeys(monkeys_data)
    worry_divider = get_worry_divider(monkeys)
    throw_items(monkeys, 10000, worry_divider, False)
    monkeys_activity = get_monkeys_activity(monkeys)

    print("Answer 2: {}".format(monkeys_activity[0] * monkeys_activity[1]))

def get_monkeys_activity(monkeys):
    monkeys_activity = [monkey.get_inspection_count() for monkey in monkeys]
    monkeys_activity.sort(reverse=True)
    return monkeys_activity

def throw_items(monkeys, rounds_num, worry_divider=1, is_auto_manage_worry=True):
    for i in range(rounds_num):
        for monkey in monkeys:
            monkey.throw_items(worry_divider, is_auto_manage_worry)

def get_worry_divider(monkeys):
    divider = 1
    for monkey in monkeys:
        divider *= monkey.get_divisible_by()
    return divider

def extract_monkeys_data(monkeys_input):
    monkeys_data = []
    curr_monkey_data = []
    for i, monkey_line in enumerate(monkeys_input):
        if i == len(monkeys_input) - 1:
            curr_monkey_data.append(monkey_line)
            monkeys_data.append(curr_monkey_data)
        elif monkey_line == "":
            monkeys_data.append(curr_monkey_data)
            curr_monkey_data = []
        else:
            curr_monkey_data.append(monkey_line)

    return monkeys_data

def parse_monkeys(monkeys_data):
    monkeys_list = []
    for monkey_data in monkeys_data:
        curr_monkey = Monkey()
        monkeys_list.append(curr_monkey)

    for i, monkey_data in enumerate(monkeys_data):
        monkeys_list[i].parse_monkey(monkey_data, monkeys_list)

    return monkeys_list
    

main()
