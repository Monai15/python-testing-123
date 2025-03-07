from coe_number.random_utils import guess_int, guess_float
import unittest
from unittest.mock import patch


class TestRandomUtils(unittest.TestCase):
    # ทดสอบ guess_int
    def test_guess_int_range(self):
        start = 1
        stop = 10
        result = guess_int(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLessEqual(result, stop)
        self.assertIsInstance(result, int)

    # ทดสอบ guess_float
    def test_guess_float_range(self):
        start = 1.0
        stop = 5.0
        result = guess_float(start, stop)
        self.assertGreaterEqual(result, start)
        self.assertLess(result, stop)
        self.assertIsInstance(result, float)

    # ใช้ Mock เพื่อควบคุมค่าสุ่ม (Advanced)
    @patch("random.randint")
    def test_guess_int_with_mock(self, mock_randint):
        mock_randint.return_value = 5
        self.assertEqual(guess_int(1, 10), 5)

    @patch("random.uniform")
    def test_guess_float_with_mock(self, mock_uniform):
        mock_uniform.return_value = 3.5
        self.assertEqual(guess_float(1.0, 5.0), 3.5)
