from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min = 99999
        for i in range(len(prices)):
            if min > prices[i]:
                min= prices[i]
            for k in prices[i+1:]:
                if k > prices[i] and ans < (k - prices[i]):
                    ans = (k - prices[i])
        return ans

instance = Solution()
res= instance.maxProfit([2,4,1])
print(res)
res= instance.maxProfit([7,6,4,3,1])
print(res)
res= instance.maxProfit([7,1,5,3,6,4])
print(res)