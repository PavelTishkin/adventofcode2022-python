class Tree:

    def __init__(self, height):
        self.height = height
        self.neighbours = {}
        self.neighbours["left"] = None
        self.neighbours["right"] = None
        self.neighbours["up"] = None
        self.neighbours["down"] = None
        self.scenic_score = 0
        self.is_visible = False

    def get_height(self):
        return self.height

    def set_neighbour(self, tree, direction):
        self.neighbours[direction] = tree

    def get_neighbour(self, direction):
        return self.neighbours[direction]

    def set_scenic_score(self, scenic_score):
        self.scenic_score = scenic_score

    def get_scenic_score(self):
        return self.scenic_score

    def get_is_visible(self):
        return self.is_visible

    def set_is_visible(self, is_visible):
        self.is_visible = is_visible


def main():
    input_file = open('input/day8.txt', 'r')
    trees_input = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    trees_map = parse_tree_map(trees_input)
    mark_visible_trees(trees_map)

    print("Answer 1: {}".format(count_visible(trees_map)))

    print("Answer 2: {}".format(get_max_scenic_score(trees_map)))

def parse_tree_map(trees_input):
    tree_map = []
    for y, trees_row_input in enumerate(trees_input):
        tree_map.append([])
        for x, tree_input in enumerate(trees_row_input):
            tree = Tree(int(tree_input))
            tree_map[y].append(tree)
            if x > 0:
                tree_map[y][x-1].set_neighbour(tree, "right")
                tree.set_neighbour(tree_map[y][x-1], "left")
            if y > 0:
                tree_map[y-1][x].set_neighbour(tree, "down")
                tree.set_neighbour(tree_map[y-1][x], "up")

    return tree_map

def mark_visible_trees(tree_map):
    mark_is_visible(tree_map[0], "down")
    mark_is_visible(tree_map[-1], "up")
    mark_is_visible([row[0] for row in tree_map], "right")
    mark_is_visible([row[-1] for row in tree_map], "left")

def mark_is_visible(tree_row, direction):
    for tree in tree_row:
        tree.set_is_visible(True)
        max_height = tree.get_height()
        curr_tree = tree.get_neighbour(direction)
        while curr_tree is not None:
            if curr_tree.get_height() > max_height:
                curr_tree.set_is_visible(True)
                max_height = curr_tree.get_height()
            curr_tree = curr_tree.get_neighbour(direction)

def get_max_scenic_score(tree_map):
    max_scenic_score = 0
    for tree_row in tree_map:
        for tree in tree_row:
            curr_scenic_score = calc_scenic_score(tree)
            if curr_scenic_score > max_scenic_score:
                max_scenic_score = curr_scenic_score

    return max_scenic_score

def calc_scenic_score(tree):
    return calc_direction_scenic_score(tree, "up") * \
        calc_direction_scenic_score(tree, "down") * \
        calc_direction_scenic_score(tree, "right") * \
        calc_direction_scenic_score(tree, "left")

def calc_direction_scenic_score(tree, direction):
    score = 0
    curr_tree = tree.get_neighbour(direction)
    while curr_tree is not None:
        score += 1
        if curr_tree.get_height() >= tree.get_height():
            curr_tree = None
        else:
            curr_tree = curr_tree.get_neighbour(direction)

    return score

def count_visible(tree_map):
    visible_count = 0
    for tree_row in tree_map:
        for tree in tree_row:
            if tree.get_is_visible():
                visible_count += 1

    return visible_count

main()
