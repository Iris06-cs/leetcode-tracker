class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # buy=0
        # sell=1
        # while sell<len(prices):
        #     if prices[buy]<prices[sell]:
        #         curr_profit=prices[sell]-prices[buy]
        #         profit=max(profit,curr_profit)
        #     else:
        #         buy=sell
        #     sell+=1
        # return profit
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
        
        
        
        
        
        

        