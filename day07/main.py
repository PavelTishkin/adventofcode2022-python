class Directory:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirectories = []
        self.files = []

    def get_name(self):
        return self.name

    def contains_directory(self, name):
        for d in self.subdirectories:
            if d.get_name() == name:
                return True
        return False

    def get_directory(self, name):
        for d in self.subdirectories:
            if d.get_name() == name:
                return d
        return None

    def get_directories(self):
        return self.subdirectories

    def add_directory(self, dir):
        self.subdirectories.append(dir)

    def contains_file(self, name):
        for f in self.files:
            if f.name == name:
                return True
        return False

    def get_file(self, name):
        for f in self.files:
            if f.name == name:
                return f
        return None

    def add_file(self, file):
        self.files.append(file)

    def get_size(self):
        total_size = 0
        for file in self.files:
            total_size += file.get_size()
        for dir in self.subdirectories:
            total_size += dir.get_size()
        
        return total_size

    def get_full_path(self):
        if self.parent == None:
            return self.name
        else:
            return self.parent.get_full_path + self.name + "/"

    def __str__(self):
        return "Path: {}; {} directories; {} files".format(
            self.get_full_path(),
            len(self.subdirectories),
            len(self.files))

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

def main():
    input_file = open('input/day7.txt', 'r')
    terminal_lines = list(map(lambda l: l.strip(), input_file.readlines()))
    root_dir = parse_fs(terminal_lines)

    print("Answer 1: {}".format(calc_dir_total_size_sum(root_dir, 100000)))

    total_disk_space = 70000000
    min_free_space = 30000000
    print("Answer 2: {}".format(find_smallest_needed_size(root_dir, root_dir.get_size(), min_free_space - (total_disk_space - root_dir.get_size()))))

def parse_fs(terminal_lines):
    root_dir = Directory("/", None)
    curr_dir = root_dir

    for terminal_line in terminal_lines:
        # Instruction line
        if terminal_line.startswith("$"):
            curr_dir = process_command(terminal_line[2:], curr_dir, root_dir)
        # Result line
        else:
            process_ls_output(terminal_line, curr_dir)

    return root_dir
            
def process_command(command, curr_dir, root_dir):
    if command.startswith("cd"):
        target = command[3:]
        if target == "/":
            return root_dir
        elif target == "..":
            return curr_dir.parent
        else:
            return curr_dir.get_directory(target)            
    elif command.startswith("ls"):
        return curr_dir
    else:
        raise Exception("Unknown command: {}".format(command))

def process_ls_output(ls_output, curr_dir):
    if ls_output.startswith("dir"):
        target = ls_output[4:]
        if not curr_dir.contains_directory(target):
            new_dir = Directory(target, curr_dir)
            curr_dir.add_directory(new_dir)
    else:
        split_output = ls_output.split(" ")
        size = int(split_output[0].strip())
        file_name = split_output[1].strip()
        if not curr_dir.contains_file(file_name):
            new_file = File(file_name, size)
            curr_dir.add_file(new_file)

def calc_dir_total_size_sum(curr_dir, max_size):
    size_sum = 0
    if curr_dir.get_size() <= max_size:
        size_sum += curr_dir.get_size()
    for sub_dir in curr_dir.get_directories():
        size_sum += calc_dir_total_size_sum(sub_dir, max_size)

    return size_sum

def find_smallest_needed_size(curr_dir, smallest_dir_size, unused_space_needed):
    new_smallest_dir_size = smallest_dir_size
    curr_dir_size = curr_dir.get_size()

    if curr_dir_size > unused_space_needed and curr_dir_size < smallest_dir_size:
        new_smallest_dir_size = curr_dir_size
    
    for dir in curr_dir.get_directories():
        new_smallest_dir_size = find_smallest_needed_size(dir, new_smallest_dir_size, unused_space_needed)

    return new_smallest_dir_size

main()
