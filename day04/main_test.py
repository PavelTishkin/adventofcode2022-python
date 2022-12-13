import unittest

from day04 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.pairs = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
            ]

    def test_get_pair_assignments_returns_correct_range(self):
        actual = main.get_pair_assignment("2-4,6-8")
        self.assertEqual(actual[0], [2, 3, 4])
        self.assertEqual(actual[1], [6, 7, 8])

    def test_is_fully_contains_returns_true_when_first_in_second(self):
        self.assertTrue(main.is_fully_contains([[2, 3], [1, 2, 3, 4]]))

    def test_is_fully_contains_returns_true_when_second_in_first(self):
        self.assertTrue(main.is_fully_contains([[1, 2, 3, 4], [2, 3]]))

    def test_is_fully_contains_returns_false_when_not_contained(self):
        self.assertFalse(main.is_fully_contains([[2, 3], [1, 2]]))

    def test_get_contain_count_returns_correct_count(self):
        pair_assignments = main.get_all_assignments(self.pairs)
        actual = main.get_contain_count(pair_assignments)
        self.assertEqual(actual, 2)

    def test_is_overlaps_returns_true_when_ranges_overlap(self):
        self.assertTrue(main.is_overlaps([[2, 3], [1, 2]]))

    def test_is_overlaps_returns_false_when_ranges_do_not_overlap(self):
        self.assertFalse(main.is_overlaps([[1, 2], [3, 4]]))

    def test_get_overlap_count_returns_correct_count(self):
        pair_assignments = main.get_all_assignments(self.pairs)
        actual = main.get_overlap_count(pair_assignments)
        self.assertEqual(actual, 4)
