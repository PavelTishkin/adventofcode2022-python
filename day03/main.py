from functools import reduce

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    input_file = open('input/day3.txt', 'r')
    rucksack_contents = list(map(lambda l: l.strip(), input_file.readlines()))

    print("Answer 1: {}".format(get_priorities_sum(rucksack_contents)))

    print("Answer 2: {}".format(get_group_badge_sum(rucksack_contents)))

def get_shared_letter(line):
    half1 = set(line[0:int(len(line)/2)])
    half2 = set(line[int(len(line)/2):])

    return list(half1.intersection(half2))[0]

def get_priority_value(letter):
    return priority.index(letter) + 1

def get_priorities_sum(rucksack_contents):
    priorities_total = 0
    for rucksack_content in rucksack_contents:
        priorities_total += get_priority_value(get_shared_letter(rucksack_content))
    
    return priorities_total

def get_group_shared_letter(group):
    shared_set = reduce(lambda x,y: set(x).intersection(set(y)), group)
    return list(shared_set)[0]

def get_group_badge_sum(rucksack_contents):
    badges_total = 0
    for i in range(0, len(rucksack_contents), 3):
        badge = get_group_shared_letter(rucksack_contents[i:i+3])
        badges_total += get_priority_value(badge)

    return badges_total

main()
