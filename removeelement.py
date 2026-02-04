from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums:
            if i == val:
                nums.remove(i)
        return len(nums),nums

instance = Solution()
print(instance.removeElement([3,2,2,3],3))

thislist = [0,1,2,2,3,4,4,5]
for i in range(len(thislist)-1):
    print(thislist[i])
    if thislist[i] == 2:
          thislist.pop(i)
print(thislist)