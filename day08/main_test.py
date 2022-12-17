import unittest

from day08 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.trees_input = [
            "30373",
            "25512",
            "65332",
            "33549",
            "35390"
        ]

    def test_parse_tree_map_populates_height_correctly(self):
        tree_map = main.parse_tree_map(self.trees_input)
        self.assertEqual(tree_map[0][0].get_height(), 3)
        self.assertEqual(tree_map[1][2].get_height(), 5)
        self.assertEqual(tree_map[4][4].get_height(), 0)

    def test_parse_tree_map_populates_neighbours_correctly(self):
        tree_map = main.parse_tree_map(self.trees_input)
        self.assertEqual(tree_map[0][0].get_neighbour("left"), None)
        self.assertEqual(tree_map[0][0].get_neighbour("up"), None)
        self.assertEqual(tree_map[0][0].get_neighbour("right").get_height(), 0)
        self.assertEqual(tree_map[0][0].get_neighbour("down").get_height(), 2)

    def test_mark_is_visible_marks_trees_correctly(self):
        tree_map = main.parse_tree_map(self.trees_input)
        main.mark_visible_trees(tree_map)
        self.assertTrue(tree_map[0][0].get_is_visible())
        self.assertFalse(tree_map[2][2].get_is_visible())

    def test_count_visible_returns_correct_value(self):
        tree_map = main.parse_tree_map(self.trees_input)
        main.mark_visible_trees(tree_map)
        actual = main.count_visible(tree_map)
        self.assertEqual(actual, 21)

    def test_calculate_scenic_score_returns_correct_value1(self):
        tree_map = main.parse_tree_map(self.trees_input)
        actual = main.calc_scenic_score(tree_map[1][2])
        self.assertEqual(actual, 4)

    def test_calculate_scenic_score_returns_correct_value2(self):
        tree_map = main.parse_tree_map(self.trees_input)
        actual = main.calc_scenic_score(tree_map[3][2])
        self.assertEqual(actual, 8)
