from coe_number.two_characters import alternate
import unittest


class TestTwoCharacters(unittest.TestCase):
    def test_give_beabeefeab_should_return_5(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_give_ababab_should_return_6(self):
        self.assertEqual(alternate("ababab"), 6)

    def test_give_aaaa_should_return_0(self):
        self.assertEqual(alternate("aaaa"), 0)

    def test_give_ab_should_return_2(self):
        self.assertEqual(alternate("ab"), 2)

    def test_give_abcabc_should_return_4(self):
        self.assertEqual(alternate("abcabc"), 4)
