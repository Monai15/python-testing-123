from coe_number.grid_challenge import gridChallenge
import unittest


class TestGridChallenge(unittest.TestCase):
    def test_give_sorted_grid_should_return_yes(self):
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")

    def test_give_unsorted_columns_should_return_no(self):
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")

    def test_give_single_row_should_return_yes(self):
        self.assertEqual(gridChallenge(["bac"]), "YES")

    def test_give_two_rows_sorted_columns_yes(self):
        self.assertEqual(gridChallenge(["bac", "def"]), "YES")
