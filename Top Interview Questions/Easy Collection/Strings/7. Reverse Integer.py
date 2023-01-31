import unittest


class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = 321
        self.assertEqual(expected, Solution().reverse(123))

    def test_second(self):
        expected = -321
        self.assertEqual(expected, Solution().reverse(-123))

    def test_third(self):
        expected = 21
        self.assertEqual(expected, Solution().reverse(120))


if __name__ == "__main__":
    unittest.main()
