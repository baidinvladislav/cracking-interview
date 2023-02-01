import unittest


class Solution:
    def reverse(self, x: int) -> int:
        to_str = str(abs(x))
        reversed_str = to_str[::-1]
        result = int(reversed_str)
        return -result if x < 0 else result


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
