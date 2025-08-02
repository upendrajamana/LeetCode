class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit=0
        min_ele=float("inf")
        for ele in prices:
            if ele<min_ele:
                min_ele=ele
            current_profit=ele-min_ele
            profit=max(current_profit,profit)
        return profit
            


