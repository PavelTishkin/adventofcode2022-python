import unittest

from day10 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        input_file = open('input/day10_test.txt', 'r')
        self.instructions = list(map(lambda l: l.strip(), input_file.readlines()))
        input_file.close()

    def test_process_instructions_returns_correct_sum(self):
        actual = main.process_instructions(self.instructions)[0]
        self.assertEqual(actual, 13140)

    def test_process_instructions_output_image(self):
        image_lines = main.process_instructions(self.instructions)[1]
        for line in image_lines:
            print(line)
