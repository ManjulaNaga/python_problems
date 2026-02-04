#removeDuplicate.py
def removeDuplicates(nums):
    i = 0
    for j in range(1,len(nums)-1):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    expectedNums = nums
    print(nums)
    return i+1


#k = removeDuplicates(nums) // Calls your implementation

#for ( i = 0; i < k; i++) {
#    nums[i] == expectedNums[i];
#}

removeDuplicates([1,1,2])


#print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))