from coe_number.caesar_cipher import caesarCipher
import unittest


class TestCaesarCipher(unittest.TestCase):
    def test_give_middle_outz_k2_should_return_okffng_qwvb(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_give_XYZ_k3_should_return_ABC(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_give_abc123_k26_should_return_abc123(self):
        self.assertEqual(caesarCipher("abc123!", 26), "abc123!")

    def test_give_z_k1_should_return_a(self):
        self.assertEqual(caesarCipher("z", 1), "a")

    def test_give_empty_string(self):
        self.assertEqual(caesarCipher("", 5), "")
