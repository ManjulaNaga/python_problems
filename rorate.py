#rotate.py
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = nums[-k:] + nums[:len(nums)-k]
        print(nums1)
        ########################
        for i in range(k):   
            n = len(nums)-1    
            t = nums[n]
            #print(t)
            while n > 0:
                nums[n] = nums[n-1]
                n -= 1
            nums[0] = t
        print(nums)
        #########################
        

instance = Solution()
instance.rotate([1,2,3,4,5,6,7],3)
