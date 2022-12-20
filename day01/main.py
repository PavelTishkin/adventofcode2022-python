from functools import reduce

def main():
    input_file = open('input/day1.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    elf_calories = []
    current_elf_calories = []
    for line in file_lines:
        if line == '':
            elf_calories.append(current_elf_calories)
            current_elf_calories = []
        else:
            current_elf_calories.append(int(line))
    
    print("Answer 1: {}".format(get_calories_sum_sorted(elf_calories)[0]))

    print("Answer 2: {}".format(get_calories_sum_sorted(elf_calories)[0] +
        get_calories_sum_sorted(elf_calories)[1] +
        get_calories_sum_sorted(elf_calories)[2]))

def get_calories_sum_sorted(elf_calories):
    calories_sum = []

    for calories in elf_calories:
        calories_sum.append(reduce(lambda x, y: x+y, calories))

    calories_sum.sort(reverse=True)

    return calories_sum

main()
