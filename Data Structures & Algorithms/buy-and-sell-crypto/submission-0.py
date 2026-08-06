class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0

        res = float("-inf")
        for r, num in enumerate(prices):
            if num <= prices[l]:
                l = r
            res = max(res, num - prices[l])
        return res