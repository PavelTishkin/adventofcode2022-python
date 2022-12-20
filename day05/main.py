import re

def main():
    input_file = open('input/day5.txt', 'r')
    file_lines = list(map(lambda l: l.rstrip(), input_file.readlines()))
    input_file.close()
    [crates, instructions] = parse_data(file_lines)
    move_all_crates(crates, instructions)

    print("Answer 1: {}".format(get_state(crates)))

    input_file = open('input/day5.txt', 'r')
    file_lines = list(map(lambda l: l.rstrip(), input_file.readlines()))
    [crates, instructions] = parse_data(file_lines)
    move_all_crates(crates, instructions, False)

    print("Answer 2: {}".format(get_state(crates)))

def parse_data(input_data):
    crates = {}
    instructions = []

    is_curr_crates = True
    for line in input_data:
        if line == "" or line.startswith(" 1"):
            is_curr_crates = False
            continue

        if is_curr_crates:
            for i in range(1, len(line), 4):
                curr_index = int((i-1)/4) + 1
                if line[i] != " ":
                    if curr_index not in crates:
                        crates[curr_index] = []
                    crates[curr_index].insert(0, line[i])
        else:
            m = re.findall("(\d+)", line)
            instructions.append([int(m[0]), int(m[1]), int(m[2])])

    return crates, instructions

def move_all_crates(crates, instructions, is_reverse=True):
    for instruction in instructions:
        move_crates(crates, instruction, is_reverse)

def move_crates(crates, instruction, is_reverse=True):
    [num_crates, from_pile, to_pile] = instruction
    moved_crates = crates[from_pile][-1*num_crates:]
    crates[from_pile] = crates[from_pile][0:-1*num_crates]
    if is_reverse:
        moved_crates.reverse()
    crates[to_pile].extend(moved_crates)

def get_state(crates):
    state = ""
    for i in range(1, len(crates) + 1):
        stack = crates[i]
        state += stack[len(stack) - 1]

    return state

main()
