import unittest

from day07 import main

class MainTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.terminal_io = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k"]

    def test_fs_root_contains_file(self):
        root_dir = main.parse_fs(self.terminal_io)
        self.assertTrue(root_dir.contains_file("b.txt"))
        f = root_dir.get_file("b.txt")
        self.assertEqual(f.get_size(), 14848514)

    def test_get_dir_e_size_is_correct(self):
        root_dir = main.parse_fs(self.terminal_io)
        actual = root_dir.get_directory("a").get_directory("e").get_size()
        self.assertEqual(actual, 584)

    def test_get_dir_a_size_is_correct(self):
        root_dir = main.parse_fs(self.terminal_io)
        actual = root_dir.get_directory("a").get_size()
        self.assertEqual(actual, 94853)

    def test_get_dir_d_size_is_correct(self):
        root_dir = main.parse_fs(self.terminal_io)
        actual = root_dir.get_directory("d").get_size()
        self.assertEqual(actual, 24933642)

    def test_get_root_dir_size_is_correct(self):
        root_dir = main.parse_fs(self.terminal_io)
        actual = root_dir.get_size()
        self.assertEqual(actual, 48381165)

    def test_calc_dir_total_size_sum_returns_correct_value(self):
        root_dir = main.parse_fs(self.terminal_io)
        actual = main.calc_dir_total_size_sum(root_dir, 100000)
        self.assertEqual(actual, 95437)

    def test_find_smallest_needed_size_returns_correct_value(self):
        root_dir = main.parse_fs(self.terminal_io)
        total_disk_space = 70000000
        min_free_space = 30000000
        actual = main.find_smallest_needed_size(root_dir, root_dir.get_size(), min_free_space - (total_disk_space - root_dir.get_size()))
        self.assertEqual(actual, 24933642)
