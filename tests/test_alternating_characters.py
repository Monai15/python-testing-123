from coe_number.alternating_characters import alternatingCharacters
import unittest


class TestAlternatingCharacters(unittest.TestCase):
    def test_give_AAAA_should_return_3(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_give_ABABABAB_should_return_0(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)

    def test_give_AAABBB_should_return_4(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_give_single_char_should_return_0(self):
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_give_empty_string_should_return_0(self):
        self.assertEqual(alternatingCharacters(""), 0)
