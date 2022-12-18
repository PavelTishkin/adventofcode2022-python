class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return "({}:{})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.get_x() and self.y == other.get_y()

    def __hash__(self):
        return hash("{}:{}".format(self.x, self.y))

class Rope():

    def __init__(self, rope_length=2):
        self.knots = []
        self.knots_visited = []
        for i in range(rope_length):
            self.knots.append(Point())
            self.knots_visited.append([Point()])

    def get_knot(self, pos):
        return self.knots[pos]

    def set_knot(self, knot, knot_pos):
        self.knots[knot_pos] = knot

    def is_knots_touch(self, knot_pos1, knot_pos2):
        return abs(self.knots[knot_pos1].get_x() - self.knots[knot_pos2].get_x()) <= 1 and abs(self.knots[knot_pos1].get_y() - self.knots[knot_pos2].get_y()) <= 1

    def move_head(self, direction):
        if direction == "R":
            self.knots[0] = Point(self.knots[0].get_x() + 1, self.knots[0].get_y())
        elif direction == "L":
            self.knots[0] = Point(self.knots[0].get_x() - 1, self.knots[0].get_y())
        elif direction == "U":
            self.knots[0] = Point(self.knots[0].get_x(), self.knots[0].get_y() + 1)
        elif direction == "D":
            self.knots[0] = Point(self.knots[0].get_x(), self.knots[0].get_y() - 1)
        else:
            raise Exception("Unknown direction: {}".format(direction))
        self.knots_visited[0].append(self.knots[0])

    def pull_tail(self):
        for i in range(1, len(self.knots)):            
            new_x, new_y = self.knots[i].get_x(), self.knots[i].get_y()
            if not self.is_knots_touch(i, i-1):
                if self.knots[i - 1].get_x() - self.knots[i].get_x() > 0:
                    new_x = self.knots[i].get_x() + 1
                elif self.knots[i - 1].get_x() - self.knots[i].get_x() < 0:
                    new_x = self.knots[i].get_x() - 1
                else:
                    new_x = self.knots[i].get_x()
                
                if self.knots[i - 1].get_y() - self.knots[i].get_y() > 0:
                    new_y = self.knots[i].get_y() + 1
                elif self.knots[i - 1].get_y() - self.knots[i].get_y() < 0:
                    new_y = self.knots[i].get_y() - 1
                else:
                    new_y = self.knots[i].get_y()
        
            self.knots[i] = Point(new_x, new_y)
            self.knots_visited[i].append(self.knots[i])

    def count_tail_visited_points(self, knot_pos):
        return len(set(self.knots_visited[knot_pos]))

def main():
    input_file = open('input/day9.txt', 'r')
    moves_input = list(map(lambda l: l.strip(), input_file.readlines()))

    rope = process_moves(moves_input, 10)
    print("Answer 1: {}".format(rope.count_tail_visited_points(1)))

    print("Answer 2: {}".format(rope.count_tail_visited_points(9)))


def process_moves(moves_input, rope_length):
    rope = Rope(rope_length)
    for move in moves_input:
        move_data = move.split(" ")
        direction = move_data[0]
        steps = int(move_data[1])
        for i in range(steps):
            rope.move_head(direction)
            rope.pull_tail()

    return rope

main()
