import unittest


class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


class TestContainsDuplicate(unittest.TestCase):
    def test_first(self):
        self.assertEqual(5, Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))

    def test_second(self):
        self.assertEqual(0, Solution().maxProfit(prices=[7, 6, 4, 3, 1]))


if __name__ == "__main__":
    unittest.main()
