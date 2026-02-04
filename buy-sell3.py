class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        if len(prices) == 2:
            return (max(prices[1]-prices[0],0))
        if len(prices)%2==0:
            mid_i = int(len(prices)/2 -1 )
        else:
            mid_i = int((len(prices) -1)/2)
        #print("len = ",len(prices))
        #print(mid_i)
        buy = prices[0]
        profit_l = 0
        for i in prices[1:mid_i+1]:
            #print(i)
            if i < buy:
                buy = i
            profit_l = max(profit_l,i-buy)
        #print("profit_l = ",profit_l)
        
        sell = prices[len(prices)-1]
        #print("sell ",sell)
        profit_r = 0
        for k in prices[:mid_i-1:-1]:
            #print(k)
            if k > sell:
                sell = k
            profit_r = max(profit_r,sell-k)
        #print("profit_r = ",profit_r) 
        return (profit_r+profit_l)
