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

class MapPoint(Point):

    def __init__(self, x, y, height, shortest_path=-1):
        Point.__init__(self, x, y)
        self.height = height
        self.neighbours = {}
        self.neighbours["left"] = None
        self.neighbours["right"] = None
        self.neighbours["up"] = None
        self.neighbours["down"] = None
        self.shortest_path = shortest_path

    def set_neighbour(self, point, direction):
        self.neighbours[direction] = point

    def get_neighbour(self, direction):
        return self.neighbours[direction]

    def get_height(self):
        return self.height

    def get_shortest_path(self):
        return self.shortest_path

    def set_shortest_path(self, shortest_path):
        self.shortest_path = shortest_path

class Map:

    def __init__(self):
        self.start = None
        self.end = None
        self.points = []
        self.mapped_points = {}

    def init_mapping(self, start):
        self.start = start
        self.end = self.points[self.end.get_y()][self.end.get_x()]
        self.mapped_points = {}
        self.mapped_points[0] = [self.start]
        for points_row in self.points:
            for point in points_row:
                point.set_shortest_path(-1)
        self.start.set_shortest_path(1)

    def calc_next_paths_step(self):
        longest_length = sorted(list(self.mapped_points.keys()))[-1]
        next_mapped_points = []
        for furthest_point in self.mapped_points[longest_length]:
            for direction in ["left", "right", "up", "down"]:
                next_point = furthest_point.get_neighbour(direction)
                if next_point is not None and next_point.get_height() <= furthest_point.get_height() + 1 and next_point.get_shortest_path() == -1:
                    next_point.set_shortest_path(longest_length + 1)
                    next_mapped_points.append(next_point)
        if len(next_mapped_points) > 0:
            self.mapped_points[longest_length + 1] = next_mapped_points
            return True
        return False

    def print_distance_map(self):
        for points_row in self.get_points():
            for point in points_row:
                print("[{:02d}]".format(point.get_shortest_path()), end="")
            print("")

    def get_start(self):
        return self.start

    def set_start(self, start):
        self.start = start

    def get_end(self):
        return self.end

    def set_end(self, end):
        self.end = end

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

def main():
    input_file = open('input/day12.txt', 'r')
    map_input = list(map(lambda l: l.strip(), input_file.readlines()))

    points_map, lowest_points = parse_map(map_input)

    points_map.init_mapping(points_map.get_start())
    while points_map.get_end().get_shortest_path() < 0:
        points_map.calc_next_paths_step()

    print("Answer 1: {}".format(points_map.get_end().get_shortest_path()))

    print("Answer 2: {}".format(find_shortest_from_lowest(points_map, lowest_points)))

def find_shortest_from_lowest(points_map, lowest_points):
    shortest = -1

    for i, lowest_point in enumerate(lowest_points):
        points_map.init_mapping(lowest_point)
        while points_map.get_end().get_shortest_path() < 0 and points_map.calc_next_paths_step():
            pass
        if points_map.get_end().get_shortest_path() != -1:
            if shortest == -1 or points_map.get_end().get_shortest_path() < shortest:
                shortest = points_map.get_end().get_shortest_path()

    return shortest

def parse_map(map_input):
    points_map = Map()
    points = []
    lowest_points = []
    start_point, end_point = None, None
    for y, line in enumerate(map_input):
        points.append([])
        for x, height in enumerate(line):
            if height == "S":
                map_point = MapPoint(x, y, 1, 1)
                points_map.set_start(map_point)
            elif height == "E":
                map_point = MapPoint(x, y, 26)
                points_map.set_end(map_point)
            else:
                map_point = MapPoint(x, y, ord(height) - 96)
            points[y].append(map_point)
            if map_point.get_height() == 1:
                lowest_points.append(map_point)
            if x > 0:
                points[y][x-1].set_neighbour(map_point, "right")
                map_point.set_neighbour(points[y][x-1], "left")
            if y > 0:
                points[y-1][x].set_neighbour(map_point, "down")
                map_point.set_neighbour(points[y-1][x], "up")

    points_map.set_points(points)
    return points_map, lowest_points

main()
