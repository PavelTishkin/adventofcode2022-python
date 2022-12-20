import unittest

from day11 import main
from day11.main import Monkey

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        input_file = open('input/day11_test.txt', 'r')
        self.monkeys_input = list(map(lambda l: l.strip(), input_file.readlines()))
        input_file.close()

    def test_parse_monkeys_data_returns_correct_number_of_monkeys(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        self.assertTrue(len(monkeys), 4)

    def test_parse_monkeys_sets_monkey_number_correctly(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        self.assertEqual(monkeys[0].get_monkey_number(), 0)
        self.assertEqual(monkeys[1].get_monkey_number(), 1)
        self.assertEqual(monkeys[2].get_monkey_number(), 2)
        self.assertEqual(monkeys[3].get_monkey_number(), 3)

    def test_parse_monkeys_sets_items_correctly(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        self.assertEqual(monkeys[0].get_items(), [79, 98])
        self.assertEqual(monkeys[1].get_items(), [54, 65, 75, 74])
        self.assertEqual(monkeys[2].get_items(), [79, 60, 97])
        self.assertEqual(monkeys[3].get_items(), [74])

    def test_parse_monkeys_sets_operation_correctly(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        self.assertEqual(monkeys[0].get_operation(), "old * 19")
        self.assertEqual(monkeys[1].get_operation(), "old + 6")
        self.assertEqual(monkeys[2].get_operation(), "old * old")
        self.assertEqual(monkeys[3].get_operation(), "old + 3")

    def test_parse_monkeys_sets_divisible_by_correctly(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        self.assertEqual(monkeys[0].get_divisible_by(), 23)
        self.assertEqual(monkeys[1].get_divisible_by(), 19)
        self.assertEqual(monkeys[2].get_divisible_by(), 13)
        self.assertEqual(monkeys[3].get_divisible_by(), 17)

    def test_parse_monkeys_sets_next_monkeys_correctly(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        self.assertEqual(monkeys[0].get_true_monkey().get_monkey_number(), 2)
        self.assertEqual(monkeys[0].get_false_monkey().get_monkey_number(), 3)
        self.assertEqual(monkeys[1].get_true_monkey().get_monkey_number(), 2)
        self.assertEqual(monkeys[1].get_false_monkey().get_monkey_number(), 0)
        self.assertEqual(monkeys[2].get_true_monkey().get_monkey_number(), 1)
        self.assertEqual(monkeys[2].get_false_monkey().get_monkey_number(), 3)
        self.assertEqual(monkeys[3].get_true_monkey().get_monkey_number(), 0)
        self.assertEqual(monkeys[3].get_false_monkey().get_monkey_number(), 1)

    def test_throw_items_produces_correct_items_allocation(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        main.throw_items(monkeys, 20)
        self.assertEqual(monkeys[0].get_items(), [10, 12, 14, 26, 34])
        self.assertEqual(monkeys[1].get_items(), [245, 93, 53, 199, 115])
        self.assertEqual(monkeys[2].get_items(), [])
        self.assertEqual(monkeys[3].get_items(), [])

    def test_get_monkeys_activity_produces_correct_result(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        main.throw_items(monkeys, 20)
        monkeys_activity = main.get_monkeys_activity(monkeys)
        self.assertEqual(monkeys_activity[0] * monkeys_activity[1], 10605)

    def test_get_monkeys_activity_with_worry_divider_produces_correct_result(self):
        monkeys_data = main.extract_monkeys_data(self.monkeys_input)
        monkeys = main.parse_monkeys(monkeys_data)
        worry_divider = main.get_worry_divider(monkeys)
        main.throw_items(monkeys, 10000, worry_divider, False)
        monkeys_activity = main.get_monkeys_activity(monkeys)
        self.assertEqual(monkeys_activity[0] * monkeys_activity[1], 2713310158)