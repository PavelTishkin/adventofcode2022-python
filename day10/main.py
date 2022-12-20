def main():
    input_file = open('input/day10.txt', 'r')
    instructions = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    strength, image_lines = process_instructions(instructions)
    print("Answer 1: {}".format(strength))

    print("Answer 2:")
    for line in image_lines:
        print(line)
    print("")

def process_instructions(instructions):
    result = 0
    image = ""

    x = 1
    cycle = 0
    ptr = 0
    is_first_add_cycle = True

    while ptr < len(instructions):
        if cycle % 40 == x or cycle % 40 == x + 1 or cycle % 40 == x - 1:
            image += "█"
        else:
            image += " "

        cycle += 1

        if (cycle - 20) % 40 == 0:
            # print("Cycle: {}; strength: {}".format(cycle, x * cycle))
            result += cycle * x

        instruction = instructions[ptr]
        # print("Cycle: {}; instruction: {}; x: {}".format(cycle, instruction, x))
        if instruction == "noop":
            ptr += 1
        else:
            instruction_data = instruction.split(" ")
            instruction_value = int(instruction_data[1])
            if is_first_add_cycle:
                is_first_add_cycle = False
            else:
                ptr += 1
                is_first_add_cycle = True
                x += instruction_value

    return result, [image[i:i+40] for i in range(0, len(image), 40)]

main()
