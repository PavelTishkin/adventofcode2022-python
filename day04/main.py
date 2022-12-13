def main():
    input_file = open('input/day4.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))
    pair_assignments = get_all_assignments(file_lines)

    print("Answer 1: {}".format(get_contain_count(pair_assignments)))

    print("Answer 2: {}".format(get_overlap_count(pair_assignments)))

def get_all_assignments(lines):
    pair_assignments = []
    for line in lines:
        pair_assignments.append(get_pair_assignment(line))

    return pair_assignments

def get_pair_assignment(line):
    pairs = line.split(',')
    pair1 = pairs[0]
    pair2 = pairs[1]
    pair1_range = pair1.split('-')
    pair2_range = pair2.split('-')
    pair_ass_1 = [*range(int(pair1_range[0]), int(pair1_range[1]) + 1, 1)]
    pair_ass_2 = [*range(int(pair2_range[0]), int(pair2_range[1]) + 1, 1)]

    return [pair_ass_1, pair_ass_2]

def get_contain_count(pair_assignments):
    count = 0
    for pair_assignment in pair_assignments:
        if is_fully_contains(pair_assignment):
            count += 1

    return count

def get_overlap_count(pair_assignments):
    count = 0
    for pair_assignment in pair_assignments:
        if is_overlaps(pair_assignment):
            count += 1

    return count

def is_fully_contains(pair_assignment):
    return set(pair_assignment[0]).issubset(set(pair_assignment[1])) or set(pair_assignment[1]).issubset(set(pair_assignment[0]))

def is_overlaps(pair_assignment):
    return not set(pair_assignment[0]).isdisjoint(set(pair_assignment[1]))

main()
