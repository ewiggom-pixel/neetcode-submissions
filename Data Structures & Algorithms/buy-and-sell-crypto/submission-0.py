class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L, profit = 0,0
        R = L + 1
        for R in range(len(prices)):

            if prices[R] < prices[L]:
                L = R
                
           
               
            money = prices[R] - prices[L]

            profit = max(profit, money)
        return profit
            
        

                
