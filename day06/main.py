def main():
    input_file = open('input/day6.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))

    print("Answer 1: {}".format(get_marker(file_lines[0], 4)))

    print("Answer 2: {}".format(get_marker(file_lines[0], 14)))

def get_marker(buffer, str_len):
    for i in range(0, len(buffer) - str_len + 1):
        test_marker = buffer[i:i+str_len]
        if len(set(test_marker)) == str_len:
            return i + str_len
    return 0

main()
