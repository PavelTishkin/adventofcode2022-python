import unittest

from day12 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.map_input = [
            "Sabqponm",
            "abcryxxl",
            "accszExk",
            "acctuvwj",
            "abdefghi"
        ]

    def test_parse_map_populates_height_correctly(self):
        map, _ = main.parse_map(self.map_input)
        self.assertEqual(map.get_points()[0][0].get_height(), 1)
        self.assertEqual(map.get_points()[2][5].get_height(), 26)
        self.assertEqual(map.get_points()[3][3].get_height(), 20)

    def test_parse_map_populates_neighbours_correctly(self):
        map, _ = main.parse_map(self.map_input)
        self.assertEqual(map.get_points()[0][0].get_neighbour("left"), None)
        self.assertEqual(map.get_points()[0][0].get_neighbour("up"), None)
        self.assertEqual(map.get_points()[0][0].get_neighbour("right").get_height(), 1)
        self.assertEqual(map.get_points()[0][0].get_neighbour("down").get_height(), 1)

    def test_calc_path_results_in_correct_length_to_end(self):
        map, _ = main.parse_map(self.map_input)
        map.init_mapping(map.get_start())
        while map.get_end().get_shortest_path() < 0:
            map.calc_next_paths_step()
        self.assertEqual(map.get_end().get_shortest_path(), 31)

    def test_calc_shortest_from_lowest_results_in_correct_length_to_end(self):
        map, lowest_points = main.parse_map(self.map_input)
        actual = main.find_shortest_from_lowest(map, lowest_points)
        self.assertEqual(actual, 29)
