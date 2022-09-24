class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        b = 0
        s = 0
        
        while (s < len(prices)):
            profit = prices[s]-prices[b]
            # if negative profit, means there is a better day to buy (lower value)
            if profit < 0:
                b = s
            # new day to sell
            elif profit > max_profit:
                max_profit = profit
            # continue from the lowest day to buy
            s += 1
            
        return max_profit