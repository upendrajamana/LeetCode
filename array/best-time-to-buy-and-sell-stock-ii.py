class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        low=prices[0]
        high=prices[0]
        n=len(prices)
        profit=0
        while i<n-1:
            while i<n-1 and prices[i]>=prices[i+1]:
                i+=1
            low=prices[i]
            while i<n-1 and prices[i]<=prices[i+1]:
                i+=1
            high=prices[i]
            profit+=high-low
        return profit
            
            