import unittest

from day03 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.rucksack_contents = ["vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]

    def test_get_shared_letter_returns_correct_letter(self):
        actual = main.get_shared_letter("vJrwpWtwJgWrhcsFMMfFFhFp")
        self.assertEqual(actual, 'p')
    
    def test_get_priority_returns_correct_value(self):
        actual = main.get_priority_value('p')
        self.assertEqual(actual, 16)

    def test_count_rucksack_values_returns_correct_sum(self):
        actual = main.get_priorities_sum(self.rucksack_contents)
        self.assertEqual(actual, 157)

    def test_get_group_shared_letter_returns_correct_letter(self):
        actual = main.get_group_shared_letter(self.rucksack_contents[0:3])
        self.assertEqual(actual, 'r')

    def test_get_group_badge_values_returns_correct_sum(self):
        actual = main.get_group_badge_sum(self.rucksack_contents)
        self.assertEqual(actual, 70)
