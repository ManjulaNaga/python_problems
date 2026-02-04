#majorityElement.py
from typing import List
class Solution:   
    def majorityElement(self, nums: List[int]) -> int:
            res = dict()
            ct = 1
            nums.sort()
            print(len(nums))
            n=len(nums)
            even_res= int(n/2-1)
            print(even_res)
            odd_res=int((n-1)/2)
            print(odd_res)
            if len(nums)%2 ==0:
                 return nums[even_res]
            else:
                 return nums[odd_res]
            n=round(len(nums)/2)
            print("n=",n)
            for i in nums:
                if i == i+1:
                    ct += 1
                    print(ct)
                else:
                    res[i] = ct
            print(res)        
            for k,v in res.items():
                if v > n:
                    print("v is "+v)
            print(k)
            return k

instance = Solution()
res= instance.majorityElement([2,2,1,1,1,2,2])
print(res)