import unittest

from day01 import main

class MainTestCase(unittest.TestCase):

    def test_get_calories_sum_sorted_return_correct_result(self):
        input_list = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]
        actual = main.get_calories_sum_sorted(input_list)
        self.assertEqual(actual, [24000, 11000, 10000, 6000, 4000])

if __name__ == '__main__':
    unittest.main()
