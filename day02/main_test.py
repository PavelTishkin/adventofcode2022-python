import unittest

from day02 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.game_rules = [["A", "Y"], ["B", "X"], ["C", "Z"]]

    def test_get_score_calculates_win_correctly(self):
        actual = main.get_hand_score(["A", "Y"])
        self.assertEqual(actual, 8)

    def test_get_score_calculates_draw_correctly(self):
        actual = main.get_hand_score(["C", "Z"])
        self.assertEqual(actual, 6)

    def test_get_score_calculates_loss_correctly(self):
        actual = main.get_hand_score(["B", "X"])
        self.assertEqual(actual, 1)
    
    def test_get_hand_score_comparison_returns_correct_result(self):
        actual = main.get_hand_score_sum(self.game_rules)
        self.assertEqual(actual, 15)

    def test_get_outcome_score_calculates_win_correctly(self):
        actual = main.get_outcome_score(["A", "Z"])
        self.assertEqual(actual, 8)
    
    def test_get_outcome_score_calculates_draw_correctly(self):
        actual = main.get_outcome_score(["B", "Y"])
        self.assertEqual(actual, 5)

    def test_get_outcome_score_calculates_loss_correctly(self):
        actual = main.get_outcome_score(["C", "X"])
        self.assertEqual(actual, 2)

    def test_get_outcome_score_comparison_returns_correct_result(self):
        actual = main.get_outcome_score_sum(self.game_rules)
        self.assertEqual(actual, 12)
    

if __name__ == '__main__':
    unittest.main()
